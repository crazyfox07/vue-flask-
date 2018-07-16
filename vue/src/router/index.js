import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: resolve =>require(['@/components/HelloWorld'],resolve)
    },
    {
      path: '/newcontact', // 和router-link to相呼应，导航到/newcontact
      name: 'NewContact',
      component: resolve =>require(['@/components/NewContact'],resolve)
    },
    {
      path: '/userinfo', // 和router-link to相呼应，导航到/newcontact
      name: 'UserInfoForm',
      component: resolve =>require(['@/components/UserInfoForm'],resolve)
    },
    {
      path: '/table-list', // 和router-link to相呼应，导航到/newcontact
      name: 'TableList',
      component: resolve =>require(['@/components/TableList'],resolve)
    }
  ]
})
