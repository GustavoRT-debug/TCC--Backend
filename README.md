# Sistema de Detecção de Expressões Faciais em Tempo Real com MediaPipe

## Funcionalidades
- Captura de vídeo em tempo real via webcam.
- Detecção de 468 pontos faciais com MediaPipe.
- Classificação de expressões faciais (feliz, triste, neutro, raiva).
- Codificação das emoções em 2 bits para otimização de memória.
- Exibição de pontos faciais e emoções na janela de vídeo.
- Salvamento dos pontos e bits em um arquivo texto (`output.txt`).
- Encerramento da captura ao pressionar a tecla 'q'.


- Python 3.8, 3.9, 3.10 ou 3.11 (Python 3.12 pode ter incompatibilidades com algumas bibliotecas).
- Webcam funcional conectada ao computador.
- Conexão com a internet para instalação das dependências.
- Espaço em disco: ~500 MB para o ambiente virtual e dependências.

## Passos para Instalação
Siga estas instruções para configurar o projeto no Windows:

1. **Clone o Repositório**:
   - Baixe o projeto ou clone-o usando Git:
     ```bash

2. **Instale o Python (se necessário)**:
   - Verifique se o Python 3.8, 3.9, 3.10 ou 3.11 está instalado:
     ```bash
     python --version
     ```
   - Se não estiver instalado ou for Python 3.12, baixe uma versão compatível em [python.org](https://www.python.org/downloads/).
   - Durante a instalação, marque a opção **"Add Python to PATH"** e instale.

3. **Crie um Ambiente Virtual**:
   - Crie um ambiente virtual para isolar as dependências:
     ```bash
     python -m venv venv
     ```
   - Ative o ambiente virtual:
     ```bash
     .\venv\Scripts\activate
     ```
   - O prompt deve mudar para `(venv) PS C:\Users\SeuUsuario\TCC>`.

4. **Instale as Dependências**:
   - Com o ambiente virtual ativado, instale as bibliotecas necessárias:
     ```bash
     pip install opencv-python mediapipe numpy scikit-learn flask
     ```
   - Alternativamente, use o arquivo `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```
   - Isso instalará:
     - `opencv-python`: Para captura de vídeo e processamento de imagens.
     - `mediapipe`: Para detecção de pontos faciais.
     - `numpy`: Para manipulação de arrays.
     - `scikit-learn`: Para o modelo de classificação.
     - `flask`: Para futura integração com API (opcional).

5. **Verifique a Instalação**:
   - Teste se as bibliotecas foram instaladas corretamente:
     ```python
     import cv2
     import mediapipe
     import numpy
     import sklearn
     import flask
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
     - Pontos faciais desenhados em verde.
     - Emoção detectada e bits no topo (ex.: "Emoção: feliz (00)").
     - Mensagem "Nenhuma face detectada" se não houver rosto.

2. **Interaja com o Sistema**:
   - Posicione seu rosto em frente à webcam.
   - Teste diferentes expressões faciais (sorrir, franzir a testa, etc.).
   - Pressione a tecla **'q'** para encerrar.

3. **Verifique os Resultados**:
   - Os pontos faciais e bits são salvos em `output.txt` no formato:
     ```
     x1,y1,x2,y2,...,x468,y468|bits
     ```
   - Exemplo:
     ```
     100.50,150.20,102.30,152.10,...,200.40,300.20|00
     ```

## Estrutura do Projeto
- `app.py`: Script principal para captura de vídeo em tempo real.
- `detector.py`: Lógica de detecção de pontos faciais, classificação de emoções e codificação.
- `requirements.txt`: Lista de dependências.
- `output.txt`: Arquivo gerado com os pontos faciais e bits das emoções.

