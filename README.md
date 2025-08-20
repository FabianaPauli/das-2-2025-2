# das-2-2025-2

## Aula 31/07/25 – Transformação Digital na Nuvem com AWS
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

