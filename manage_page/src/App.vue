<template>
  <div id="app">
    <el-page-header content="SpotifyLyrics Settings" style="margin-bottom: 10px;"/>
    <el-form ref="form" style="margin: 5%;padding-bottom: 10px">
      <el-divider content-position="left">UI Settings</el-divider>
      <el-form-item label="Always on top(restart to take effect)">
        <el-switch
            v-model="form['always-top']"
            active-color="#13ce66"
            inactive-color="#ff4949">
        </el-switch>
      </el-form-item>
      <el-form-item label="Show background color when unlocked">
        <el-switch
            v-model="form['show-background-when-unlocked']"
            active-color="#13ce66"
            inactive-color="#ff4949">
        </el-switch>
      </el-form-item>
      <el-form-item label="Show background color when locked">
        <el-switch
            v-model="form['show-background-when-locked']"
            active-color="#13ce66"
            inactive-color="#ff4949">
        </el-switch>
      </el-form-item>
      <el-form-item label="Background color">
        <el-color-picker v-model="backgroundcolor" size="medium" :show-alpha="true" color-format="rgb" @change="updateBackgroundColor"></el-color-picker>
      </el-form-item>
      <el-divider content-position="left">Text Settings</el-divider>
      <el-form-item label="Text color">
        <el-color-picker v-model="fontcolor" size="medium" :show-alpha="false" color-format="rgb" @change="updateFontColor"></el-color-picker>
      </el-form-item>
      <el-form-item label="Text-stroke color">
        <el-color-picker v-model="strokecolor" size="medium" :show-alpha="false" color-format="rgb" @change="updateStrokeColor"></el-color-picker>
      </el-form-item>
      <el-form-item label="Font family">
        <el-select v-model="form['font-family']" filterable>
          <el-option
              v-for="item in fonts"
              :key="item.name"
              :label="item.name"
              :value="item.name">
          </el-option>
        </el-select>
      </el-form-item>
      <el-divider content-position="left">System Settings - Non-professionals do not modify</el-divider>
      <el-form-item label="Spotify developer client id">
        <el-input v-model="form['client-id']"></el-input>
      </el-form-item>
      <el-form-item label="Spotify developer client secret">
        <el-input v-model="form['client-secret']"></el-input>
      </el-form-item>
      <el-divider content-position="left">Cache Settings - Non-professionals do not modify</el-divider>
      <el-form-item label="Spotify user refresh token">
        <el-input v-model="form['refresh-token']"></el-input>
      </el-form-item>
      <el-form-item label="Musixmatch user token">
        <el-input v-model="form['musixmatch-token']"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submit">Save</el-button>
      </el-form-item>
    </el-form>
    <el-backtop :visibility-height="10"></el-backtop>
    <div class="copyright">
      <div class="c_top">
        <div class="xh">Made<br>with love</div>
      </div>
      <div>2022.12</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'SpotifyLyrics',
  data() {
    return {
      timer: null,
      fontcolor: '',
      strokecolor: '',
      backgroundcolor: '',
      fonts: [],
      form: {
        'font-color': {
          'r': 0,
          'g': 0,
          'b': 0,
        },
        'font-effect-color': {
          'r': 0,
          'g': 0,
          'b': 0,
        },
        'background-color': {
          'r': 0,
          'g': 0,
          'b': 0,
          'a': 0.2
        },
        'font-family': "",
        'refresh-token': "",
        'musixmatch-token': "",
        'always-top': true,
        'client-id': "",
        'client-secret': "",
        'show-background-when-locked': false,
        'show-background-when-unlocked': false,
      }
    };
  },
  created() {
    this.get_settings()
  },
  mounted() {
    document.title = 'SpotifyLyrics Settings'
  },
  methods: {
    submit(){
      if (!this.form["client-id"]) {
        this.$message.warning("Invalid client id")
        return
      }
      if (!this.form["client-secret"]) {
        this.$message.warning("Invalid client secret")
        return
      }
      if (!this.form["font-family"]) {
        this.$message.warning("Invalid client secret")
        return
      }
      axios.request({
        method: 'post',
        url:'http://127.0.0.1:60001/update_settings',
        data: this.form
      }).then((res) => {
        if (res.data.success) {
          this.$message.success("Settings saved.")
        }
      }).catch(() => {
        this.$message.error("Save failed.")
      })
    },
    updateBackgroundColor() {
      // format rgba(123, 123, 123, 0.5)
      let transparency = Number(this.backgroundcolor.split(",")[3].split(")")[0].replace(" ", ""))
      if (transparency < 0.15 || transparency > 1.0) {
        this.$message.warning("Transparency should be above 0.15 and below 1.0")
        this.form['background-color']={
          r: this.backgroundcolor.split(",")[0].split("(")[1],
          g: this.backgroundcolor.split(",")[1].substring(1),
          b: this.backgroundcolor.split(",")[2].substring(1).split(")")[0],
          a: 0.15
        }
        this.backgroundcolor = "rgb("+this.form["background-color"].r+","+this.form["background-color"].g+","+this.form["background-color"].b+",0.15)"
        return
      }
      this.form['background-color']={
        r: this.backgroundcolor.split(",")[0].split("(")[1],
        g: this.backgroundcolor.split(",")[1].substring(1),
        b: this.backgroundcolor.split(",")[2].substring(1).split(")")[0],
        a: this.backgroundcolor.split(",")[3].split(")")[0].replace(" ", "")
      }
    },
    updateFontColor() {
      this.form['font-color']={
        r: this.fontcolor.split(",")[0].split("(")[1],
        g: this.fontcolor.split(",")[1].substring(1),
        b: this.fontcolor.split(",")[2].substring(1).split(")")[0]
      }
    },
    updateStrokeColor() {
      this.form["font-effect-color"]={
        r: this.strokecolor.split(",")[0].split("(")[1],
        g: this.strokecolor.split(",")[1].substring(1),
        b: this.strokecolor.split(",")[2].substring(1).split(")")[0]
      }
    },
    get_settings() {
      axios.get("http://127.0.0.1:60001/settings").then((data) => {
        this.form = data.data
        this.fontcolor = "rgb("+this.form["font-color"].r+","+this.form["font-color"].g+","+this.form["font-color"].b+")"
        this.strokecolor = "rgb("+this.form["font-effect-color"].r+","+this.form["font-effect-color"].g+","+this.form["font-effect-color"].b+")"
        this.backgroundcolor = "rgb("+this.form["background-color"].r+","+this.form["background-color"].g+","+this.form["background-color"].b+","+this.form['background-color'].a+")"
      }).catch(() => {
        this.$message.error("Request failed")
      })
      axios.get("http://127.0.0.1:60001/installed_fonts").then((data) => {
        data.data.fonts.forEach(i => {
          this.fonts.push({
            name: i
          })
        })
      }).catch(() => {
        this.$message.error("Request failed")
      })
    }
  }
}
</script>
<style>
#app {
  margin: 25px;
}

.el-page-header__left {
  display: none !important;
}

.xh {
  font-size: 15px;
  padding-left: 15px;
  padding-top: 5px;
}

.copyright {
  margin-top: 15px;
  user-select: none;
  width: 100%;
  text-align: center;
  font-size: 12px;
  color: #555;
}

.c_top {
  display: inline-block;
  height: 70px;
  padding-top: 19px;
  padding-left: 75px;
  font-size: 17px;

  vertical-align: top;
  background: url(~@/assets/images/xh.png) no-repeat left center;
  background-size: contain;
}
</style>
