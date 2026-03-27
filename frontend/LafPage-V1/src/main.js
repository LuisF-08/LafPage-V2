import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from './router'

// arquivo que inicilaiza logicamente todo o o sistemas 
// que  vue cria , alem de ser onde se cadastras as rotas
// do vue-router efetivamente

createApp(App)
  .use(router)
  .mount('#app')