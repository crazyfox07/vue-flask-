import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import NewContact from '@/components/NewContact'
import UserInfoForm from '@/components/UserInfoForm'
import TableList from '@/components/TableList'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/newcontact', // 和router-link to相呼应，导航到/newcontact
      name: 'NewContact',
      component: NewContact
    },
    {
      path: '/userinfo', // 和router-link to相呼应，导航到/newcontact
      name: 'NewContact',
      component: UserInfoForm
    },
    {
      path: '/table-list', // 和router-link to相呼应，导航到/newcontact
      name: 'table-list',
      component: TableList
    }
  ]
})
