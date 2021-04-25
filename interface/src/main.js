import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import axios from 'axios'
import Va from 'vue-atlas'
import 'vue-atlas/dist/vue-atlas.css'


// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(axios)
// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.use(Va, 'en') 

Vue.config.productionTip = false

// 앱을 마운트할때 라우터를 쓸수있는거 
new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
