import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'
import Main from '@/components/main'
import report from '@/components/report'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '',
      name: 'home',
      component: home,
      children:[
         {path:"/",name:'main',component:Main},
         {path:"/report",name:'report',component:report},
      ]
    }
  ],
  mode:'history',
})
