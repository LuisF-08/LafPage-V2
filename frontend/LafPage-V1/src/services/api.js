const API_URL = 'http://localhost:8000';

export async function enviarCodigo(email) {
  const res = await fetch(`${API_URL}/enviar-codigo`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  });

  return res.json();
}

export async function validarCodigo(email, codigo) {
  const res = await fetch(`${API_URL}/validar-codigo`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, codigo })
  });

  return res.json();
}

export async function validarCNPJ(cnpj) {
  const res = await fetch(`${API_URL}/validar-cnpj`, {
    method:'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ cnpj })
  });

  return res.json();
  
}