import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import Vuetify from 'vuetify/lib'
import axios from 'axios'
import VueApexCharts from 'vue-apexcharts'
Vue.use(VueApexCharts)
import VideoPlayer from 'vue-video-player'
require('video.js/dist/video-js.css')
require('vue-video-player/src/custom-theme.css')
Vue.use(VideoPlayer)
import 'videojs-contrib-hls'
const hls = require('videojs-contrib-hls')
Vue.use(hls)
import 'element-theme-chalk/lib/index.css';
import { Network } from "vue-vis-network";
Vue.component('network', Network);
import '@fortawesome/fontawesome-free/css/all.css' // Ensure you are using css-loader
import VueMasonry from 'vue-masonry-css'
Vue.use(VueMasonry);

Vue.use(Vuetify)


axios.defaults.baseURL = 'http://34.95.230.124:8000'


Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  axios,
  VueApexCharts,
  Network,
  render: h => h(App)
}).$mount('#app')
