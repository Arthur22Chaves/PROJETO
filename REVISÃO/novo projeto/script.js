const inputPesquisa = document.getElementById('input-pesquisa');
inputPesquisa.addEventListener('change', async () => {
  const corPesquisada = inputPesquisa.value;
  const sugestoes = await getSugestoesIAGemini(corPesquisada);
  exibirSugestoesIAGemini(sugestoes);
});