<template>
  <footer class="footer">
    <div class="container footer-content">
      <div class="cards-wrapper">
        <div class="card-duvidas">
          <h4 class="text-[20px] md:text-[60px] h-40 text-center text-6xl md:text-5xl lg:text-6xl 
            bg-gradient-to-r from-blue-400 via-green-400 to-sky-300
            bg-clip-text text-transparent
            tracking-tight
            leading-tight
            max-w-5xl"
          >Quer nos conhecer?</h4>
            <nav class="footer-nav">
                <ul>
                  <li><router-link to="/"><i class="fa-solid fa-house-chimney-window"></i> Home</router-link></li>
                  <li><router-link to="/nosso-catalogo"><i class="fa-solid fa-heart-pulse"></i>Catálogo</router-link></li>
                  <li><router-link to="/sac"><i class="fa-solid fa-headset"></i> SAC</router-link></li>
                  <li><router-link to="/trabalho"><i class="fa-solid fa-person-digging"></i> Trabalhe Conosco</router-link></li>
                  <li><router-link to="/parceiros-nossos"><i class="fa-solid fa-industry"></i>Nossos Parceiros</router-link></li>
                </ul>
            </nav>
        </div>
        <div class ="card-contato">
         <h4 class="text-[20px] md:text-[60px] h-40 text-center text-6xl md:text-5xl lg:text-6xl 
            bg-gradient-to-r from-blue-400 via-green-400 to-sky-300
            bg-clip-text text-transparent
            tracking-tight
            leading-tight
            max-w-5xl"
          >Não encontrou o que precisava? Fale em nossas</h4>
             <ul class="icons-list">
                <li><a href="https://wa.me/558005910367"><i class="fa-brands fa-whatsapp"></i></a></li>
                <li><a href="https://www.instagram.com/lafmeddistribuidora"><i class="fa-brands fa-instagram"></i></a></li>
                <li><a href="https://www.facebook.com/lafmeddistribuidora"><i class="fa-brands fa-facebook-f"></i></a></li>
                <li><a href="https://br.linkedin.com/in/lafmed-distribuidora-farmac%C3%AAutica-840619248"><i class="fa-brands fa-linkedin-in"></i></a></li>
             </ul>
        </div>
      </div>
        <div class ="container-info">
            <p>Av. Juracy Magalhães, 1177 - Boa Vista</p>
            <p>Vitória da Conquista - BA, 45026-090</p>
            <button @click="abrirMapa">
            📍 Não encontrou? clique aqui !
            </button>
        </div>
    <div class="end">
      <h4>LAFMED Distribuidora Farmacêutica</h4>
      <h4>®Todos os direitos reservados. © 2023</h4>
      <p>...</p>
      <img class="logo" :src="logo" alt="imagem da logo da empesa">
    </div>
    </div>
  </footer>
</template>

<script setup >
import logo from "../assets/logo.png";

function abrirMapa() {
  window.open(
    "https://www.google.com/maps/place/Lafmed+Distribuidora+Farmac%C3%AAutica/@-14.8754515,-40.843922,17z",
    "_blank"
  )
}
</script>

<style>

:root {
  --primary-color: #117ae4;
  --accent-color: #1699e6;
  --text-light: #f8fafc;
}

.footer {
  background-color: var(--primary-color);;
  text-align: center;
  padding: 40px 20px;
  width: 100%;
  z-index: 1000;
  display: flex;
  height: auto;
  margin-top: 40px;
  position: relative;
  left: 0;
  border-top: 3px solid transparent;
  border-image: linear-gradient(to right, transparent, var(--accent-color), transparent) 1;
}

.footer-content{
display: flex;
flex-direction: column;
gap: 30px;
max-width: 1200px;
margin: 0 auto;
}

.cards-wrapper{
  display: flex;
  flex-direction: row; 
  gap: 30px;
  width: 100%;
}


.footer-nav ul{
  display: flex;
  flex-direction: column;
  gap: 15px;
  padding: 0;
  list-style: none;
  align-items: center; 
}

.footer-nav a{
  color: #ffffff;
  font-size: 1.2rem;
  text-decoration: none;
  padding: 12px 25px;
  border-radius: 50px;
  background: rgba(255, 255, 255, 0.1); 
  border: 1px solid rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  width: fit-content;
  min-width: 220px; 
}

.footer-nav a i {
  font-size: 1.1rem;
  color: #16e6ca;
}

.footer-nav a:hover{
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
  transform: scale(1.05) translateY(-3px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  border-color: #16e6ca;
}


.card-duvidas, .card-contato{
  flex: 1;
  color: white;
  padding: 30px;
  border-radius: 20px;
  box-sizing: border-box;
  margin-bottom: 10px;
  font-style: italic;
  font-size: larger;
}

.card-contato{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.container-info{
  color: rgb(255, 255, 255);
  padding: 15px;
  border-top: 1px solid;
  border-image: linear-gradient(to right, transparent, #ccc, transparent) 1;
}

.container-info button{
  padding: 10px;
  border-radius: 10px;
  color: #ffffff;
  font-size: 1.2rem;
  text-decoration: none;
  border-radius: 50px;
  background: rgba(255, 255, 255, 0.1); 
  border: 1px solid rgba(255, 255, 255, 0.2);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  width: fit-content;
  min-width: 220px; 

}

.container-info button:hover{
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
  transform: scale(1.05) translateY(-3px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  border-color: #16e6ca;
}

.end{
  color: rgb(255, 255, 255);
  border-radius: 20px;
  padding-top: 20px;
  border-top: 1px solid;
  border-image: linear-gradient(to right, transparent, #ccc, transparent) 1;
}

.icons-list {
  list-style: none;
  display: flex;
  gap: 25px; 
  flex-direction: row;
  padding: 20px 0;
  justify-content: center;
  align-items: center;
}

.icons-list li {
  animation: flutuar 3s ease-in-out infinite;
}

.icons-list li:nth-child(1) { animation-delay: 0s; }
.icons-list li:nth-child(2) { animation-delay: 0.4s; }
.icons-list li:nth-child(3) { animation-delay: 0.8s; }
.icons-list li:nth-child(4) { animation-delay: 1.2s; }

.icons-list a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  font-size: 28px;
  color: #ffffff;
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(5px);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}


.icons-list li:hover a .fa-whatsapp {
  color: #25D366;
  filter: drop-shadow(0 0 10px rgba(37, 211, 102, 0.5));
}
.icons-list li:hover a:has(.fa-whatsapp) {
  border-color: #25D366;
  background: rgba(37, 211, 102, 0.1);
  transform: scale(1.2) translateY(-10px);
}


.icons-list li:hover a .fa-instagram {
  color: #E1306C;
  filter: drop-shadow(0 0 10px rgba(225, 48, 108, 0.5));
}
.icons-list li:hover a:has(.fa-instagram) {
  border-color: #E1306C;
  background: rgba(225, 48, 108, 0.1);
  transform: scale(1.2) translateY(-10px);
}


.icons-list li:hover a .fa-facebook-f {
  color: #0044ff;
  filter: drop-shadow(0 0 10px rgba(24, 119, 242, 0.5));
}
.icons-list li:hover a:has(.fa-facebook-f) {
  border-color: #0044ff;
  background: rgba(24, 119, 242, 0.1);
  transform: scale(1.2) translateY(-10px);
}


.icons-list li:hover a .fa-linkedin-in {
  color: #d6d6d6;
  filter: drop-shadow(0 0 10px rgba(0, 119, 181, 0.5));
}
.icons-list li:hover a:has(.fa-linkedin-in) {
  border-color: #d6d6d6;
  background: rgba(0, 119, 181, 0.1);
  transform: scale(1.2) translateY(-10px);
}

.logo{
  height: 70px;
  width: auto;
  margin-left: auto;
  margin-right: auto;
  filter: brightness(0) invert(1) drop-shadow(0 2px 4px rgba(255, 255, 255, 0.2));
  transition: all 0.3s ease;
}

.footer-nav ul {
  display: flex;
  flex-direction: column;
  gap: 15px;
  padding: 0;
  list-style: none;
  align-items: center;
}

.footer-nav li {
  /* Faz cada botão flutuar individualmente com tempos diferentes para um efeito orgânico */
  animation: flutuar 4s ease-in-out infinite;
  width: 100%;
  display: flex;
  justify-content: center;
}


.footer-nav li:nth-child(2) { animation-delay: 0.5s; }
.footer-nav li:nth-child(3) { animation-delay: 1s; }
.footer-nav li:nth-child(4) { animation-delay: 1.5s; }

.footer-nav a {
  color: #ffffff;
  font-size: 1.2rem;
  text-decoration: none;
  padding: 12px 25px;
  border-radius: 50px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.3s ease;
  min-width: 240px;
  justify-content: center;
  backdrop-filter: blur(5px);
}


.footer-nav a:hover {
  background: #16e6ca; 
  color: #0d4a85;      
  transform: scale(1.1) translateY(-5px); 
  box-shadow: 0 15px 30px rgba(22, 230, 202, 0.4);
  border-color: #ffffff;
}

.footer-nav a i {
  transition: transform 0.3s ease;
}

.footer-nav a:hover i {
  transform: rotate(15px);
  color: #0d4a85;
}

/*  MOBILE  */
@media (max-width: 768px) {
  .footer-nav a {
    font-size: 1.5rem; 
    padding: 18px 30px;
    width: 90%;
  }
  .icons-list {
    gap: 15px;
  }
  .icons-list a {
    width: 55px;
    height: 55px;
    font-size: 24px;
  }
  .cards-wrapper {
    flex-direction: column; 
  }
}
</style>