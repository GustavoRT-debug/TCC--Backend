# Sistema de Detecção de Emoções Positivas/Negativas em Tempo Real com DeepFace

## Descrição

Este projeto é um sistema em Python desenvolvido como Trabalho de Conclusão de Curso (TCC) que detecta emoções faciais em tempo real usando a webcam. Ele utiliza a biblioteca **DeepFace** para identificar emoções (feliz, triste, neutro, raiva, surpresa, medo, nojo) e as classifica como **positiva** (ex.: feliz, surpresa) ou **negativa** (ex.: triste, raiva, medo, nojo). As emoções são codificadas em **1 bit** (0 para positiva, 1 para negativa), facilitando a análise da experiência do usuário (UX) em interfaces digitais, indicando se o usuário "gostou" ou "não gostou". Os resultados são exibidos na janela de vídeo e salvos em um arquivo compacto (`output.txt`).

## Funcionalidades

- Captura de vídeo em tempo real via webcam.
- Detecção de emoções com DeepFace (feliz, triste, neutro, raiva, surpresa, medo, nojo).
- Classificação das emoções como positiva (0) ou negativa (1).
- Exibição da emoção, classificação e bit na janela de vídeo (ex.: "Emoção: feliz (positiva, 0)").
- Salvamento dos dados em `output.txt` (ex.: `feliz|positiva|0`).
- Encerramento da captura ao pressionar a tecla 'q'.

## Requisitos

- Sistema operacional: Windows 10/11.
- Python 3.8, 3.9, 3.10 ou 3.11 (Python 3.12 pode ter incompatibilidades com algumas bibliotecas).
- Webcam funcional conectada ao computador.
- Conexão com a internet para instalação das dependências e download de modelos DeepFace (~200 MB).
- Espaço em disco: ~1 GB para o ambiente virtual, dependências e modelos.

## Passos para Instalação

Siga estas instruções para configurar o projeto no Windows:

1. **Clone o Repositório**:

   - Baixe o projeto ou clone-o usando Git:

     ```bash
     git clone <URL_DO_REPOSITORIO>
     ```

   - Ou baixe o ZIP e extraia em uma pasta (ex.: `C:\Users\SeuUsuario\TCC`).

2. **Instale o Python (se necessário)**:

   - Verifique se o Python 3.8, 3.9, 3.10 ou 3.11 está instalado:

     ```bash
     python --version
     ```

   - Se não estiver instalado ou for Python 3.12, baixe uma versão compatível em [python.org](https://www.python.org/downloads/).

   - Durante a instalação, marque a opção **"Add Python to PATH"** e instale.

3. **Crie um Ambiente Virtual**:

   Crie um ambiente virtual para isolar as dependências:

   ```bash
   python -m venv venv
   ```

   Ativo ou ambiente virtual:

   ```bash
   .\venv\Scripts\activate
   ```

   O prompt deve mudar para `(venv) PS C:\Users\SeuUsuario\TCC>`.

4. **Instale as Dependências**:

   - Com o ambiente virtual ativado, instale as bibliotecas necessárias:

     ```bash
     pip install opencv-python deepface flask tf-keras
     ```

   - Alternativamente, use o arquivo `requirements.txt`:

     ```bash
     pip install -r requirements.txt
     ```

   - Isso instalará:

     - `opencv-python`: Para captura de vídeo e processamento de imagens.
     - `deepface`: Para detecção de emoções.
     - `flask`: Para futura integração com API (opcional).
     - `tf-keras`: Dependência necessária para DeepFace com TensorFlow.

5. **Verifique a Instalação**:

   - Teste se as bibliotecas foram instaladas corretamente:

     ```python
     import cv2
     import deepface
     import flask
     import tf_keras
     print("Todas as bibliotecas estão instaladas!")
     ```

   - Salve como `test_libs.py` e execute:

     ```bash
     python test_libs.py
     ```

   - Se não houver erros, a instalação foi bem-sucedida.

6. **Teste a Webcam**:

   - Verifique se a webcam está funcionando:

     ```python
     import cv2
     cap = cv2.VideoCapture(0)
     ret, frame = cap.read()
     if ret:
         cv2.imshow("Teste Webcam", frame)
         cv2.waitKey(0)
     else:
         print("Erro: Não foi possível abrir a webcam.")
     cap.release()
     cv2.destroyAllWindows()
     ```

   - Salve como `test_webcam.py` e execute:

     ```bash
     python test_webcam.py
     ```

   - Se uma janela com o vídeo da webcam abrir, está tudo certo. Feche com qualquer tecla.

## Uso

1. **Execute o Programa**:

   - Com o ambiente virtual ativado, inicie o sistema:

     ```bash
     python app.py
     ```

   - Uma janela abrirá mostrando o vídeo da webcam com:

     - Emoção detectada, classificação e bit no topo (ex.: "Emoção: feliz (positiva, 0)").
     - Mensagem "Emoção: neutral (positiva, 0)" se não houver rosto detectado.

2. **Interaja com o Sistema**:

   - Posicione seu rosto em frente à webcam.
   - Teste diferentes expressões faciais (sorrir, franzir a testa, etc.).
   - Pressione a tecla **'q'** para encerrar.

3. **Verifique os Resultados**:

   - As emoções, classificações e bits são salvos em `output.txt` no formato:

     ```
     emoção|classificação|bit
     ```

   - Exemplo:

     ```
     feliz|positiva|0
     triste|negativa|1
     neutral|positiva|0
     ```

## Estrutura do Projeto

- `app.py`: Script principal para captura de vídeo em tempo real.
- `detector.py`: Lógica de detecção de emoções, classificação como positiva/negativa e codificação em 1 bit.
- `requirements.txt`: Lista de dependências.
- `output.txt`: Arquivo gerado com as emoções, classificações e bits.

## Limitações

- Suporta apenas uma face por frame.
- A detecção pode falhar em condições de baixa iluminação ou ângulos extremos.
- O DeepFace consome mais recursos computacionais em comparação com soluções leves.
- Requer conexão com a internet na primeira execução para baixar modelos.

## Solução de Problemas

- **Erro "Invalid requirement" no** `requirements.txt`:

  - Certifique-se de que cada biblioteca está em uma linha separada:

    ```
    deepface
    opencv-python
    flask
    tf-keras
    ```

  - Reinstale:

    ```bash
    pip install -r requirements.txt
    ```

- **Erro "ModuleNotFoundError: No module named 'cv2'"**:

  - Instale o OpenCV:

    ```bash
    pip install opencv-python
    ```

- **Erro "ModuleNotFoundError: No module named 'deepface'"**:

  - Instale o DeepFace:

    ```bash
    pip install deepface
    ```

- **Erro "ModuleNotFoundError: No module named 'tf_keras'"**:

  - Instale o tf-keras:

    ```bash
    pip install tf-keras
    ```

  - Alternativamente, downgradear o TensorFlow:

    ```bash
    pip install tensorflow==2.15.0
    ```

- **Webcam não abre**:

  - Execute `test_webcam.py` para diagnosticar.
  - Feche outros aplicativos que possam usar a webcam (ex.: Zoom, Skype).
  - Verifique as permissões em **Configurações > Privacidade > Câmera** no Windows.
  - Tente índices alternativos (ex.: `cv2.VideoCapture(1)`).

- **Lentidão no processamento**:

  - O código usa resolução reduzida (320x240). Para mais otimização:

    ```python
    cap.set(cv2.CAP_PROP_FPS, 15)
    ```

## Contribuições para o TCC

- Demonstra conhecimentos em **visão computacional** com DeepFace e OpenCV.
- Implementa uma abordagem inovadora de **classificação binária** (positiva/negativa) para análise de UX.
- Integra sistemas em **tempo real** para captura e processamento de vídeo.
- Resolve desafios técnicos, como configuração de dependências e compatibilidade.

---

### **Mudanças em Relação ao Exemplo Fornecido**

1. **Título e Descrição**:

   - Substituído "Detecção de Expressões Faciais com MediaPipe" por "Detecção de Emoções Positivas/Negativas com DeepFace".
   - Enfatizada a classificação binária para UX ("gostou" ou "não gostou").

2. **Funcionalidades**:

   - Removidas referências a pontos faciais e MediaPipe.
   - Classificação alterada de 4 emoções (feliz, triste, neutro, raiva) com 2 bits para positiva (0) ou negativa (1) com 1 bit.
   - Saída em `output.txt` mudou de pontos faciais para `emoção|classificação|bit`.

3. **Requisitos**:

   - Aumentado o espaço em disco para ~1 GB (modelos DeepFace).
   - Mantido Python 3.8-3.11.

4. **Instalação**:

   - Dependências alteradas para `opencv-python`, `deepface`, `flask`, `tf-keras`.
   - Incluídas soluções para erros enfrentados (`tf_keras`, `cv2`, `requirements.txt`).
   - Mantido o texto exato para "Crie um Ambiente Virtual" conforme sua solicitação.

5. **Uso**:

   - Atualizado para refletir a exibição de emoções/classificação/bit.
   - Exemplo de `output.txt` ajustado.

6. **Estrutura**:

   - Arquivos mantidos (`app.py`, `detector.py`, `requirements.txt`, `output.txt`).
   - Descrição ajustada para DeepFace.

7. **Solução de Problemas**:

   - Adicionados erros reais do projeto (`Invalid requirement`, `tf_keras`, `cv2`, webcam).

8. **Contribuições para o TCC**:
   - Foco na classificação binária e UX, alinhado com sua solicitação.

---

### **Verificação do Projeto**

Para garantir que o projeto funcione:

1. **Salve o README**:

   - Use o conteúdo acima em `C:\Users\gugut\OneDrive\Área de Trabalho\Repos Gustavo\TCC\README.md`.

2. **Confirme os Arquivos**:

   - Verifique que `app.py` e `detector.py` são iguais aos fornecidos.
   - `requirements.txt` deve ser:
     ```
     deepface
     opencv-python
     flask
     tf-keras
     ```

3. **Instale Dependências**:

   ```bash
   cd C:\Users\gugut\OneDrive\Área de Trabalho\Repos Gustavo\TCC
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Teste Bibliotecas**:

   ```bash
   python test_libs.py
   ```