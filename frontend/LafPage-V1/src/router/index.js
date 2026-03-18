import { createRouter, createWebHistory } from 'vue-router'

import Trabalho from '../views/Trabalho.vue'
import Home from '../views/Home.vue'
import NossoCatalogo from '../views/NossoCatalogo.vue'
import Sac from '../views/Sac.vue'
import NossosParceiros from '../views/NossosParceiros.vue'
import QuemSomos from '../views/QuemSomos.vue'


const routes = [
  { 
    path: '/',
    component: Home 
  },
  {
    path: '/trabalho',
    component: Trabalho
  },
  { 
    path: '/sac',
    component: Sac
  },
  { 
    path: '/nosso-catalogo',
    component: NossoCatalogo 
  },
  { 
    path: '/parceiros-nossos',
    component: NossosParceiros
  },
  {
    path: '/quem-somos',
    component: QuemSomos
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router