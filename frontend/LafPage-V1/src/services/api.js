// usei o axios pois ele alem de facilitar a sintaxe ele só tem uma desvantagem
//ao fech padrão que seria só o seu tamanho que aumenta um pouco
import axios from "axios";
const API_URL = import.meta.env.VITE_API_URL;
// rotas da counicação do fronte-end com vue e da
// parte do backend do node para o python(FASTAPI) até o 
// banco de dados POSTGRESQL, senhas e tudo mais no .env
// importação da url por motivos de segurança 

//função de enjvio de envio de codigo para o 
// email solicitado para confirmação
export async function enviarCodigo(email) {
  const res = await axios.post(`${API_URL}/enviar-codigo`, { email });
  return res.data;
}

//função de validação de código enviado, pedindo o
//  email e o código como para metros
export async function validarCodigo(email, codigo) {
  const res = await axios.post(`${API_URL}/validar-codigo`, { email, codigo });
  return res.data;
}

// função que alem de puxar o cnpj tendo sua formatação e inserção não permitidos 
// a não ser no formato pedido, ele valida novamente o formato via api
export async function validarCNPJ(cnpj) {
  const res = await axios.post(`${API_URL}/validar-cnpj`, { cnpj });
  return res.data;
}

// 2° validação ao cnpj, dessa vez puxando do banco o cnpj se está cadastrado
export async function validar_cnpj_no_banco(cnpj) {
    const res = await axios.post(`${API_URL}/validar-cnpj-banco`,
      {cnpj});
      return res.data;
}

// valida a nota fiscal se está atrelada à um cnpj que está cadastrado na empresa
export async function validar_nota_fiscal(notaFiscal) {
  const res = await axios.post(`${API_URL}/validar-nota-fiscal`, {
    nota_fiscal: notaFiscal});
  return res.data;
}

// cria o formulário e envia o modelo para o fastAPI(BACKEND)
export async function criar_formulario_sac(dados, arquivo) {
  const formData = new FormData();
  formData.append("dados", JSON.stringify(dados));

  if (arquivo instanceof File) {
    formData.append("arquivo", arquivo);
  }

  const res = await axios.post(`${API_URL}/sac-envio`, 
    formData, {
    headers: {
      "Content-Type": "multipart/form-data"
    }
  });

  return res.data;
}

export async function baixar_XML_nota_fiscal(cnpj) {
  return await axios.get(`${API_URL}/baixar-xml/${cnpj}`, {
    responseType: 'blob' 
  });
}

export async function buscar_notas_e_numeros(cnpj, filtros = {}){
  const params = Object.fromEntries(
    Object.entries(filtros).filter(([_, v]) => v !== '' && v != null)
  );
  const res = await axios.get(`${API_URL}/notas/${cnpj}`, {params});
  return res.data;

}

export async function buscar_boletos(cnpj, filtros = {}) {
  const params = Object.fromEntries(
    Object.entries(filtros).filter(([_, v]) => v !== '' && v != null)
  );
  const res = await axios.get(`${API_URL}/buscar-boletos/${cnpj}`, { params });
  return res.data;
}

export async function baixar_pdf_boleto(boleto_id) {
  const res = await axios.get(`${API_URL}/baixar-pdf-boleto/${boleto_id}`, {
    responseType: 'blob' 
  });
  return res.data; 
}