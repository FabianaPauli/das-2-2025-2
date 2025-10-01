# Materia DAS 2 2025-2

## Aula 30/07/25 – Transformação Digital na Nuvem com AWS

- **Motivação para Nuvem**: lidar com picos de acesso e substituir infra tradicional.  
- **Serviços iniciais**: S3 (armazenamento), SQS (mensageria) e EC2 (máquinas virtuais).  
- **Papel do arquiteto de soluções**: entender problema, criar protótipos, validar, acompanhar construção.  
- **Well-Architected Framework**: 6 pilares (operação, segurança, confiabilidade, custo, sustentabilidade, desempenho).  
- **Automação e IaC**: evitar operações manuais, usar Terraform e DevOps para escalabilidade.  
- **Segurança na nuvem**: vulnerabilidade humana, boas práticas de credenciais (MFA), simulações de ataques, rastreabilidade.  
- **Resiliência**: sistemas que se recriam sozinhos, resposta a falhas em tempo real, aumento automático de recursos.  
- **Otimização e Escalabilidade**: métricas (CPU, uso real) para ajustar recursos dinamicamente.  
- **Arquitetura distribuída**: evitar ponto único de falha, múltiplos bancos (ex.: leitura/escrita separados), backup e versionamento.  

---

## Aula 13/08/25 – Permissões e Identidade na AWS

- **Políticas de Permissão**: usuário x recurso. Negação sempre tem prioridade.  
- **Identidade e Autenticação**: documentos de identidade, cólices e AWS Cognito (armazenar e autenticar usuários, trial de 12 meses).  
- **Hospedagem em S3**: solução econômica para sites estáticos (HTML, CSS, JS). Usado em grandes eventos (ex.: Rock in Rio).  
- **Elementos de apólices**: ação, efeito, recurso, responsável (*princeton*) e condições (ex.: acesso só em certos horários ou IPs).  
- **Exemplos práticos**:  
  - Controle de fotos com restrição de IP (ex.: Dept. de Defesa).  
  - Permissão condicional para tags em servidores Minecraft.  
- **Permissões em Banco de Dados**: granularidade até nível de tabela, colisão entre políticas de conceder x remover.  
- **Conflitos de Políticas**: todas são reunidas numa requisição; ausência de autorização bloqueia ação.  
- **Créditos gratuitos AWS**: US$100 ao criar conta com cartão + período de serviços grátis.  
- **Atividades no Canvas**: módulos de Arquitetura (M2) e Segurança (M3).  

---

## Aula 20/08/25 – Arquitetura de Rede e Comunicação


### Arquitetura de Rede e Comunicação
- **Análise de arquivos e desenhos** de rede.
- Discussão sobre a **ausência de diálogo** entre elementos da rede.
- Considerações sobre **subnets públicas** e **tabelas de rotas** na AWS.

### Comunicação entre Serviços
- Acesso e **comunicação com serviços gerenciados** dentro da AWS.
- **Conexões diretas** dentro da AWS, sem passar pela internet.

### Rede Privada Virtual (VPC)
- **VPC** como rede privada para uso exclusivo dentro da AWS.
- **Cobrança por hora** e **tráfego de dados**, sem versão gratuita.

### Serviços Gratuitos de Rede
- **Serviço gratuito** para criação de **portas de rede**.
- Conexões limitadas na versão gratuita, sem **limite de tráfego** ou **banda**.
 
---
## Aula 27/08/25 – Gerenciamento e Manipulação de Arquivos na AWS

Esta aula foi uma demonstração prática de como usar o **Amazon S3** para gerenciar arquivos na nuvem. O foco principal foi a interação com o serviço, tanto pelo console da AWS quanto por código, cobrindo segurança, automação e boas práticas.

---

* **Manipulação de arquivos no S3**: Demonstração de como criar "buckets", fazer upload de arquivos programaticamente e editar conteúdo direto na plataforma. Os arquivos são tratados como **objetos binários**.
* **Permissões e acesso público**: Acesso a arquivos é privado por padrão. Para torná-los públicos, é preciso desativar o **"Bloqueio de Acesso Público"** e ajustar as permissões do bucket.
* **Políticas de acesso (Policies)**: Usamos o **"policy generator"** da AWS para criar políticas que controlam quem pode fazer o quê (ações como `ListBucket`) em recursos específicos (identificados pelo **ARN**).
* **Níveis de SDK da AWS**: A aula comparou dois níveis de abstração do kit de desenvolvimento (SDK):
    * **High-level**: Mais simples, ideal para operações básicas.
    * **Low-level**: Oferece maior controle, mas exige mais esforço.
* **Automação e IA**: A inteligência artificial foi mostrada como uma ferramenta para acelerar o desenvolvimento, gerando código e documentação. A ênfase foi na importância de entender o código, não apenas copiá-lo.
* **Limpeza do ambiente**: O encerramento da aula reforçou a necessidade de **comitar** as alterações, fazer **logout** e **limpar** o ambiente de trabalho para evitar problemas de segurança e custos.

---

## Aula 10/09/25 – Ataques e Segurança

### Ataque de Phishing Bancário
- **Fraude bancária** com site falso do **Banco do Brasil**, capturando dados bancários.
- Técnicas como **DNS similar** para redirecionar usuários.

### Proteção de Dados Bancários e CORS
- Proteção contra **fraudes** com **CORS (Cross-Origin Resource Sharing)**.
- Impede sites falsos de acessarem dados bancários.

### Configuração de Domínios Confiáveis
- Necessidade de configurar **domínios confiáveis** para **front-end**.
- Importância de restringir o acesso ao **back-end** e usar asterisco para aceitar qualquer domínio.

### Configuração e Acesso ao S3
- **Configuração do S3** em relação a **domínios** e **permissões de acesso**.

### Exposição de Dados Online: Configuração e Riscos
- **Riscos de "balde público"** no S3 e **acesso via URL**.
- Importância de desativar o **bloqueio de acesso público** em "baldes" para acesso autorizado.

### Políticas de Acesso e Desbloqueio
- **Políticas de permissão** no AWS para **acesso a recursos** e **arquivos**.

### Controle de Acesso a Arquivos
- Discussão sobre **controle de acesso** e **segurança em arquivos**.
- **Alta necessidade de segurança** em tráfego de dados.

---

## Aula 17/09/25 – Redes, Conectividade e Entrega de Conteúdo

A aula focou em como as redes funcionam na nuvem, desde a conexão de diferentes ambientes virtuais até a otimização da entrega de conteúdo.

---

#### Pontos-chave da aula:

* **Conexão de Redes**: Foram mostradas as formas de conectar redes isoladas na AWS (**VPC Peering**) e como ligar a rede de uma empresa à nuvem usando **VPNs**.
* **Conexões Seguras**: Para alta velocidade e segurança, foi apresentada a **Direct Connect**, que cria uma conexão de fibra óptica dedicada. Para manter a segurança interna, foi discutido o uso de **VPC Endpoints** para que o tráfego entre serviços da AWS, como um servidor e o **S3**, não passe pela internet.
* **Segurança (Firewalls)**: A aula diferenciou os dois firewalls da AWS: o **Security Group** (na instância) e a **NACL** (no nível da subnet), que controlam o tráfego de entrada e saída.
* **Resiliência e DNS**: Foi explicado como o **DNS** torna a internet resiliente. Ferramentas como o **Route 53** e o **Cloudflare** permitem estratégias avançadas para garantir que os usuários sempre se conectem ao servidor mais próximo e disponível.
* **Entrega de Conteúdo (CDN)**: Para acelerar a entrega de conteúdo, foi apresentado o **CloudFront**, o serviço de **CDN** da AWS. Ele armazena cópias de conteúdo em servidores próximos aos usuários (**"edge locations"**), reduzindo a latência.
---

## Aula 24/09/25 – Arquitetura de Rede e Comunicação

Esta aula explorou conceitos de arquitetura de rede, com foco em como os serviços na nuvem interagem entre si. O professor utilizou uma demonstração prática de uma aplicação web para ilustrar a comunicação entre diferentes componentes e as complexidades de uma rede virtual.

---

#### Pontos-chave da aula:

* **Arquitetura de Rede AWS**: A aula apresentou os fundamentos de uma rede na AWS, incluindo conceitos como **subnets públicas** e **tabelas de rotas**. Foi explicado como a comunicação pode ocorrer tanto pela internet (para serviços gerenciados) quanto por conexões diretas, sem exposição à internet, algo comum em grandes empresas.
* **Virtual Private Cloud (VPC)**: A **VPC** foi descrita como a "rede privada" do usuário dentro da AWS. É um serviço que permite criar uma rede virtual isolada, controlando completamente a configuração, desde o alcance de IPs até a criação de sub-redes. Diferente de outros serviços, a VPC é cobrada por hora e pelo tráfego de dados, sem uma versão gratuita.
* **Comunicação entre serviços**: A demonstração de uma aplicação web em um ambiente distribuído serviu para mostrar a comunicação entre os componentes. Mensagens eram enviadas e recebidas por um **MQTT broker**, um protocolo de comunicação leve, ideal para a Internet das Coisas (IoT) e ambientes distribuídos.
* **Protocolos e tecnologias**: A aula fez menção a protocolos industriais como o **OPTO** e a diferença entre arquiteturas de processadores como **Intel/AMD** (X86) e **ARM**, que afetam a execução de programas e containers **Docker**. Além disso, foi discutida a comunicação entre programas via **memória RAM**, um método considerado arcaico e de alto risco.
* **Estratégias de Desenvolvimento**: A aula abordou a importância de criar recursos reais, dar um bom nome a eles e entender a base de um código antes de tentar alterá-lo. Também foi destacado o uso de ferramentas como **Docker** para simplificar o empacotamento e a execução de aplicações em diferentes ambientes.
