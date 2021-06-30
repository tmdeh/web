import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main.vue'
import Introduce from '../views/Introduce.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Introduce',
    component:Introduce
  },
  {
    path: '/main',
    name: 'Main',
    component: Main
  },
]

const router = new VueRouter({
  routes
})

export default router
