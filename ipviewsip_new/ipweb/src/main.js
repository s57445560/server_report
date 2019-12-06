// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false;
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
import VueRouter from "vue-router";

import Vuex from 'vuex'
import Axios from 'axios'
Vue.use(Vuex);
Vue.prototype.$http = Axios;
Vue.http = Axios;
import VueCookies from 'vue-cookies'
Vue.use(VueCookies);
import echarts from 'echarts'

Vue.prototype.$echarts = echarts;
Vue.echarts = echarts;

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
};
/* eslint-disable no-new */
import Base from '@/components/store/base'
import Table from '@/components/store/table'

var server_host_ip_and_port = window.location.host;



const store = new Vuex.Store({
  state: {
    // request_url:"http://"+ "127.0.0.1:8000"
    request_url: ''
  },
  mutations: {
    // 用来设置升级列表的

  },
  actions:{
    // 用来获取升级列表的
  },
  modules:{
    Base,
    Table,
  }
});


Vue.filter('number',function (value) {
   return Number(value)
});


Axios.get('./static/project.config.json').then((result) => {
  console.log(result.data);
  Vue.prototype.baseConfig = result.data;
  Vue.baseConfig = result.data;
  var app = new Vue({
    el: '#app',
    router,
    store,
    components: { App },
    template: '<App/>'
  });
  window.app = app;
});



