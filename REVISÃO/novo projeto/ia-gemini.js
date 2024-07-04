async function getSugestoesIAGemini(corPesquisada) {
  // Faça a requisição à API da IA Gemini usando o fetch()
  const response = await fetch(`https://api.ia-gemini.com/sugestoes?cor=${corPesquisada}`);
  const data = await response.json();
  return data.sugestoes;
}
async function getSugestoesIAGemini(corPesquisada) {
  // Faça a requisição à API da IA Gemini usando o fetch()
  const response = await fetch(`https://api.ia-gemini.com/sugestoes?cor=${corPesquisada}`);
  const data = await response.json();
  return data.sugestoes;
}
function exibirSugestoesIAGemini(sugestoes) {
  const secaoSugestoes = document.getElementById('sugestoes-ia-gemini');
  secaoSugestoes.innerHTML = ''; // Limpar a seção antes de adicionar novos conteúdos

  sugestoes.forEach(sugestao => {
    const sugestaoElement = document.createElement('div');
    sugestaoElement.classList.add('sugestao-ia-gemini');

    sugestaoElement.innerHTML = `
      <img src="${sugestao.imagemUrl}" alt="${sugestao.descricao}">
      <p>${sugestao.descricao}</p>
    `;

    secaoSugestoes.appendChild(sugestaoElement);
  });
}
