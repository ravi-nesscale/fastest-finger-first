import { createRouter, createWebHistory } from 'vue-router'
import { session } from './data/session'
import { userResource } from '@/data/user'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  {
    name: 'Login',
    path: '/account/login',
    component: () => import('@/pages/Login.vue'),
  },
  {
    path: '/Leaderboard',
    name: 'Leaderboard',
    component: () => import('@/pages/Leaderboard.vue'),
  },
  {
    path: '/Gamesession',
    name: 'Gamesession',
    component: () => import('@/pages/Gamesession.vue'),
  },
  {
    path: '/Welcomebutton',
    name: 'Welcomebutton',
    component: () => import('@/pages/Welcomebutton.vue'),
  },
  {
    path: '/QuestionManagement',  
    name: 'QuestionManagement',
    component: () => import('@/pages/QuestionManagement.vue'),
  },
  {
    path: '/AdminControl',  
    name: 'AdminControl',
    component: () => import('@/pages/AdminControl.vue'),
  },
]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
})

router.beforeEach(async (to, from, next) => {
  let isLoggedIn = session.isLoggedIn
  try {
    await userResource.promise
  } catch (error) {
    isLoggedIn = false
  }

  if (to.name === 'Login' && isLoggedIn) {
    next({ name: 'Home' })
  } else if (to.name !== 'Login' && !isLoggedIn) {
    next({ name: 'Login' })
  } else {
    next()
  }
})

export default router
