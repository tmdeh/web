
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import kakao from '../views/kakao.vue'
import Example from '../views/Example.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path:'/kakao',
    name: 'kakao',
    component: kakao
  },
  {
    path: '/example',
    name: 'Example',
    component: Example
  },
]

const router = new VueRouter({
  routes
})

export default router
