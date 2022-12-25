import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import axios from 'axios'
import locale from 'element-ui/lib/locale/lang/en'

Vue.prototype.axios = axios;
Vue.use(ElementUI, {locale});

new Vue({
    el: '#app',
    render: h => h(App)
});
