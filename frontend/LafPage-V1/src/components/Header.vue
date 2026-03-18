<script setup>
import { ref } from 'vue';
import logo from "../assets/logo.png";

const menuOpen = ref(false);

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
}
</script>

<template>
  <header class="header">
    <div class="container">

      <!-- Logo -->
      <router-link to="/" class="logo-link">
        
        <img class="logo " :src="logo" alt="logo da página">
      </router-link>

      <!-- Menu Hamburger -->
      <button class="menu-toggle" @click="toggleMenu">
        ☰
      </button>

      <!-- Navegação -->
      <nav class="nav" :class="{ 'open': menuOpen }">
        <router-link to="/" @click="menuOpen=false">Home</router-link>
        <router-link to="/nosso-catalogo" @click="menuOpen=false">Nosso Catálogo</router-link>
        <router-link to="/sac" @click="menuOpen=false">SAC </router-link>
        <router-link to="/trabalho" @click="menuOpen=false">Trabalho </router-link>
        <router-link to="/parceiros-nossos" @click="menuOpen=false">Parceiros</router-link>
        <router-link to="/quem-somos" @click="menuOpen=false">Quem Somos</router-link>
      </nav>
      <!-- Ações (Telefone e Loja) -->
      <div class="header-actions" :class="{'actions-open': menuOpen}">
        <div class="phone">
          <router-link 
              to="/sac"
              class="btn-telefone fa-solid fa-file-invoice-dollar mr-2">
              <i class="fa-solid fa-arrows-rotate"></i>
              Boleto / 2° via
          </router-link>
        </div>
        <a href="http://lafmed.resultwebvendas.com.br/#/login" class="btn-loja fa-solid fa-cart-arrow-down">
          Compras On-line 
        </a>
      </div>

    </div>
  </header>
</template>

<style scoped>
/* Cabeçalho */
.header {
  --primary-color: #117ae4;
  --accent-color: #1699e6;
  --text-light: #f8fafc;
  background-color: var(--primary-color);
  color: var(--text-light);
  width: 100%;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  padding: 10px 40px;
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  border-bottom: 3px solid transparent;
  border-image: linear-gradient(to right, transparent, var(--accent-color), transparent) 1;
}
.header-actions {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 20px;
}

.container {
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 30px;
  display: flex;
  align-items: center;
  gap: 40px;
}

/*logo da empresa*/
.logo {
  height: 60px;
  width: auto;
  object-fit: contain;
  display: block;
  filter: brightness(0) invert(1) drop-shadow(0 2px 4px rgba(255, 255, 255, 0.2));
  transition: all 0.3s ease;
}

.logo:hover {
  transform: scale(1.08) rotate(-1deg); 
  filter: brightness(1.3) drop-shadow(0 0 15px rgba(255, 255, 255, 0.6));
}


.logo-link {
  display: flex;
  align-items: center;
}

/* Navegação Desktop (Visível por padrão) */
.nav {
  display: flex;
  gap: 30px; 
}

.nav a {
  color: var(--text-light);
  text-decoration: none;
  font-weight: 500;
  font-size: 0.95rem;
  border-radius: 10px;
  padding: 8px 0;
  position: relative;
  transition: color 0.3s ease;
}

.nav a:hover {
  color: var(--text-hover);
  transform: translateY(-1PX);
  box-shadow: 10px 8px 5px rgba(43, 36, 36, 0.3);
}

.nav a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 2px;
  background-color: var(--accent-color);
  transition: width 0.3s ease;
}

.nav a.router-link-active {
  color: var(--accent-color);
}

.nav a.router-link-active::after {
  width: 100%;
}

/* Ações Desktop ( */
.header-actions {
  display: flex;
  align-items: center;
  gap: 20px;
}

.phone {
  font-weight: 600;
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  gap: 5px;
}

.btn-loja, .btn-telefone {
  background-color: var(--accent-color);
  color: #ffffff; 
  text-decoration: none;
  padding: 8px 20px;
  border-radius: 25px; 
  cursor: pointer;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.btn-loja:hover {
  background-color: #fd9800;
  transform: translateY(-2px); 
  padding: 12px 25px;
  box-shadow: 0 4px 8px rgba(255, 255, 255, 0.3);
}

.btn-telefone:hover{
  background-color: #cf2c2c;
  padding: 12px 25px;
  transform: translateY(-2px); 
  box-shadow: 0 4px 8px rgba(255, 255, 255, 0.3);
}

/* Botão do mobile */
.menu-toggle {
  display: none;
  font-size: 28px;
  background: none;
  border: none;
  color: white;
  cursor: pointer;
  padding: 0;
}

/* MOBILE */
@media (max-width: 968px) {

  .logo{
    height: 55px;
  }

  .container{
    padding: 0 15px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between; 
    align-items: center;
  }

  .header {
    padding: 20px 0;
  }

  .header-actions{
    margin-left: 0;
  }

  .menu-toggle {
    display: block;
  }

  .nav, .header-actions {
    display: none;
    width: 100%;
    flex-direction: column;
    text-align: center;
  }

  .nav {
    margin-top: 20px;
    gap: 15px;
  }

  .header-actions {
    margin-top: 15px;
    gap: 15px;
  }

  .nav.open, .header-actions.actions-open {
    display: flex;
  }
}
</style>