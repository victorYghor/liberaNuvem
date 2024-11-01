# LiberaNuvem

![LiberaNuvem App Icon](https://github.com/user-attachments/assets/2959fa66-e725-4c6d-bc6b-bc4279780c73)

**LiberaNuvem** é uma solução para auxiliar pessoas que enfrentam desafios com a falta de espaço de armazenamento em seus dispositivos móveis. Muitos utilizam o celular como principal ferramenta de comunicação e para armazenar fotos, vídeos e informações pessoais e familiares. No entanto, limitações de orçamento e o desconhecimento sobre alternativas dificultam uma gestão eficiente desse espaço.

O objetivo do LiberaNuvem é facilitar o acesso a métodos gratuitos e eficazes para liberar e gerenciar o armazenamento em dispositivos móveis, oferecendo ferramentas e conhecimento para que todos possam aproveitar melhor o espaço de seus celulares sem depender de planos pagos.

## Como começar

Para utilizar o LiberaNuvem, é necessário ter uma chave de API da AWS. Consulte o guia [aqui para obter sua chave](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

### Configuração da Chave de API:

1. Configure sua chave de API com o comando:
   ```bash
   aws configure
   ```
2. Insira a chave de API conforme solicitado.

## Instalação

Para facilitar a instalação, incluímos um script que automatiza a configuração das dependências.

### Linux

1. Execute o comando abaixo no terminal:
   ```bash
   bash install.sh
   ```

### Windows

1. Crie um ambiente virtual:
   ```bash
   python3 -m venv venv
   ```
2. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

LiberaNuvem ajuda você a manter seu dispositivo organizado e eficiente, liberando espaço e otimizando o armazenamento de maneira prática e acessível.

---

Para testar o libera nuvem você pode usar o postmand e fazer o upload de um arquivo: ![image](https://github.com/user-attachments/assets/2c2b8687-fb60-41b6-9b9f-ca3aeca00cce)

Lembre-se de colocar sua secret-key no header: 
![image](https://github.com/user-attachments/assets/3e9f0ed3-1357-4913-a223-8716b7c9452c)

