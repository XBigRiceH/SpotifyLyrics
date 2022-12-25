(function(t){function o(o){for(var r,s,i=o[0],c=o[1],a=o[2],u=0,d=[];u<i.length;u++)s=i[u],Object.prototype.hasOwnProperty.call(l,s)&&l[s]&&d.push(l[s][0]),l[s]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(t[r]=c[r]);f&&f(o);while(d.length)d.shift()();return n.push.apply(n,a||[]),e()}function e(){for(var t,o=0;o<n.length;o++){for(var e=n[o],r=!0,i=1;i<e.length;i++){var c=e[i];0!==l[c]&&(r=!1)}r&&(n.splice(o--,1),t=s(s.s=e[0]))}return t}var r={},l={app:0},n=[];function s(o){if(r[o])return r[o].exports;var e=r[o]={i:o,l:!1,exports:{}};return t[o].call(e.exports,e,e.exports,s),e.l=!0,e.exports}s.m=t,s.c=r,s.d=function(t,o,e){s.o(t,o)||Object.defineProperty(t,o,{enumerable:!0,get:e})},s.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},s.t=function(t,o){if(1&o&&(t=s(t)),8&o)return t;if(4&o&&"object"===typeof t&&t&&t.__esModule)return t;var e=Object.create(null);if(s.r(e),Object.defineProperty(e,"default",{enumerable:!0,value:t}),2&o&&"string"!=typeof t)for(var r in t)s.d(e,r,function(o){return t[o]}.bind(null,r));return e},s.n=function(t){var o=t&&t.__esModule?function(){return t["default"]}:function(){return t};return s.d(o,"a",o),o},s.o=function(t,o){return Object.prototype.hasOwnProperty.call(t,o)},s.p="";var i=window["webpackJsonp"]=window["webpackJsonp"]||[],c=i.push.bind(i);i.push=o,i=i.slice();for(var a=0;a<i.length;a++)o(i[a]);var f=c;n.push([0,"chunk-vendors"]),e()})({0:function(t,o,e){t.exports=e("56d7")},3825:function(t,o,e){},"56d7":function(t,o,e){"use strict";e.r(o);var r=e("2b0e"),l=e("5c96"),n=e.n(l),s=(e("0fae"),function(){var t=this,o=t._self._c;return o("div",{attrs:{id:"app"}},[o("el-page-header",{staticStyle:{"margin-bottom":"10px"},attrs:{content:"SpotifyLyrics Settings"}}),o("el-form",{ref:"form",staticStyle:{margin:"5%","padding-bottom":"10px"}},[o("el-divider",{attrs:{"content-position":"left"}},[t._v("UI Settings")]),o("el-form-item",{attrs:{label:"Always on top(restart to take effect)"}},[o("el-switch",{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},model:{value:t.form["always-top"],callback:function(o){t.$set(t.form,"always-top",o)},expression:"form['always-top']"}})],1),o("el-form-item",{attrs:{label:"Show background color when unlocked"}},[o("el-switch",{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},model:{value:t.form["show-background-when-unlocked"],callback:function(o){t.$set(t.form,"show-background-when-unlocked",o)},expression:"form['show-background-when-unlocked']"}})],1),o("el-form-item",{attrs:{label:"Show background color when locked"}},[o("el-switch",{attrs:{"active-color":"#13ce66","inactive-color":"#ff4949"},model:{value:t.form["show-background-when-locked"],callback:function(o){t.$set(t.form,"show-background-when-locked",o)},expression:"form['show-background-when-locked']"}})],1),o("el-form-item",{attrs:{label:"Background color"}},[o("el-color-picker",{attrs:{size:"medium","show-alpha":!0,"color-format":"rgb"},on:{change:t.updateBackgroundColor},model:{value:t.backgroundcolor,callback:function(o){t.backgroundcolor=o},expression:"backgroundcolor"}})],1),o("el-divider",{attrs:{"content-position":"left"}},[t._v("Text Settings")]),o("el-form-item",{attrs:{label:"Text color"}},[o("el-color-picker",{attrs:{size:"medium","show-alpha":!1,"color-format":"rgb"},on:{change:t.updateFontColor},model:{value:t.fontcolor,callback:function(o){t.fontcolor=o},expression:"fontcolor"}})],1),o("el-form-item",{attrs:{label:"Text-stroke color"}},[o("el-color-picker",{attrs:{size:"medium","show-alpha":!1,"color-format":"rgb"},on:{change:t.updateStrokeColor},model:{value:t.strokecolor,callback:function(o){t.strokecolor=o},expression:"strokecolor"}})],1),o("el-form-item",{attrs:{label:"Font family"}},[o("el-select",{attrs:{filterable:""},model:{value:t.form["font-family"],callback:function(o){t.$set(t.form,"font-family",o)},expression:"form['font-family']"}},t._l(t.fonts,(function(t){return o("el-option",{key:t.name,attrs:{label:t.name,value:t.name}})})),1)],1),o("el-divider",{attrs:{"content-position":"left"}},[t._v("System Settings - Non-professionals do not modify")]),o("el-form-item",{attrs:{label:"Spotify developer client id"}},[o("el-input",{model:{value:t.form["client-id"],callback:function(o){t.$set(t.form,"client-id",o)},expression:"form['client-id']"}})],1),o("el-form-item",{attrs:{label:"Spotify developer client secret"}},[o("el-input",{model:{value:t.form["client-secret"],callback:function(o){t.$set(t.form,"client-secret",o)},expression:"form['client-secret']"}})],1),o("el-divider",{attrs:{"content-position":"left"}},[t._v("Cache Settings - Non-professionals do not modify")]),o("el-form-item",{attrs:{label:"Spotify user refresh token"}},[o("el-input",{model:{value:t.form["refresh-token"],callback:function(o){t.$set(t.form,"refresh-token",o)},expression:"form['refresh-token']"}})],1),o("el-form-item",{attrs:{label:"Musixmatch user token"}},[o("el-input",{model:{value:t.form["musixmatch-token"],callback:function(o){t.$set(t.form,"musixmatch-token",o)},expression:"form['musixmatch-token']"}})],1),o("el-form-item",[o("el-button",{attrs:{type:"primary"},on:{click:t.submit}},[t._v("Save")])],1)],1),o("el-backtop",{attrs:{"visibility-height":10}}),t._m(0)],1)}),i=[function(){var t=this,o=t._self._c;return o("div",{staticClass:"copyright"},[o("div",{staticClass:"c_top"},[o("div",{staticClass:"xh"},[t._v("Made"),o("br"),t._v("with love")])]),o("div",[t._v("2022.12")])])}],c=(e("14d9"),e("cee4")),a={name:"HomeCenterIOT",data(){return{timer:null,fontcolor:"",strokecolor:"",backgroundcolor:"",fonts:[],form:{"font-color":{r:0,g:0,b:0},"font-effect-color":{r:0,g:0,b:0},"background-color":{r:0,g:0,b:0,a:.2},"font-family":"","refresh-token":"","musixmatch-token":"","always-top":!0,"client-id":"","client-secret":"","show-background-when-locked":!1,"show-background-when-unlocked":!1}}},created(){this.get_settings()},mounted(){document.title="SpotifyLyrics Settings"},methods:{submit(){this.form["client-id"]?this.form["client-secret"]&&this.form["font-family"]?c["a"].request({method:"post",url:"http://127.0.0.1:60001/update_settings",data:this.form}).then(t=>{t.data.success&&this.$message.success("Settings saved.")}).catch(()=>{this.$message.error("Save failed.")}):this.$message.warning("Invalid client secret"):this.$message.warning("Invalid client id")},updateBackgroundColor(){let t=Number(this.backgroundcolor.split(",")[3].split(")")[0].replace(" ",""));if(t<.15||t>1)return this.$message.warning("Transparency should be above 0.15 and below 1.0"),this.form["background-color"]={r:this.backgroundcolor.split(",")[0].split("(")[1],g:this.backgroundcolor.split(",")[1].substring(1),b:this.backgroundcolor.split(",")[2].substring(1).split(")")[0],a:.15},void(this.backgroundcolor="rgb("+this.form["background-color"].r+","+this.form["background-color"].g+","+this.form["background-color"].b+",0.15)");this.form["background-color"]={r:this.backgroundcolor.split(",")[0].split("(")[1],g:this.backgroundcolor.split(",")[1].substring(1),b:this.backgroundcolor.split(",")[2].substring(1).split(")")[0],a:this.backgroundcolor.split(",")[3].split(")")[0].replace(" ","")}},updateFontColor(){this.form["font-color"]={r:this.fontcolor.split(",")[0].split("(")[1],g:this.fontcolor.split(",")[1].substring(1),b:this.fontcolor.split(",")[2].substring(1).split(")")[0]}},updateStrokeColor(){this.form["font-effect-color"]={r:this.strokecolor.split(",")[0].split("(")[1],g:this.strokecolor.split(",")[1].substring(1),b:this.strokecolor.split(",")[2].substring(1).split(")")[0]}},get_settings(){c["a"].get("http://127.0.0.1:60001/settings").then(t=>{this.form=t.data,this.fontcolor="rgb("+this.form["font-color"].r+","+this.form["font-color"].g+","+this.form["font-color"].b+")",this.strokecolor="rgb("+this.form["font-effect-color"].r+","+this.form["font-effect-color"].g+","+this.form["font-effect-color"].b+")",this.backgroundcolor="rgb("+this.form["background-color"].r+","+this.form["background-color"].g+","+this.form["background-color"].b+","+this.form["background-color"].a+")"}).catch(()=>{this.$message.error("Request failed")}),c["a"].get("http://127.0.0.1:60001/installed_fonts").then(t=>{t.data.fonts.forEach(t=>{this.fonts.push({name:t})})}).catch(()=>{this.$message.error("Request failed")})}}},f=a,u=(e("e767"),e("2877")),d=Object(u["a"])(f,s,i,!1,null,null,null),m=d.exports,p=e("b2d6"),h=e.n(p);r["default"].prototype.axios=c["a"],r["default"].use(n.a,{locale:h.a}),new r["default"]({el:"#app",render:t=>t(m)})},e767:function(t,o,e){"use strict";e("3825")}});
//# sourceMappingURL=app.ac76dfd8.js.map