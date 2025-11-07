# 🌡️ Monitoramento de Temperaturas em Tempo Real

### Sobre o Projeto

Este projeto tem como objetivo demonstrar, de forma prática, os conceitos de **Computação Distribuída** utilizando **Python**, **Flask** e **RabbitMQ**.  

A aplicação simula um sistema de **monitoramento de temperatura em tempo real**, onde um componente atua como **produtor (Producer)** e outro como **consumidor (Consumer)**.  

- O **Producer** gera valores de temperatura (simulados) e os envia para uma **fila RabbitMQ** hospedada na nuvem (CloudAMQP).  
- O **Consumer**, implementado com **Flask**, recebe essas mensagens e exibe os dados em uma interface web, permitindo acompanhar as atualizações em tempo real.  

O projeto busca evidenciar o funcionamento de uma arquitetura baseada em **mensageria**, onde há **desacoplamento** entre os componentes do sistema. Dessa forma, o produtor e o consumidor funcionam de maneira independente, comunicando-se apenas por meio da fila.  

Essa abordagem é amplamente utilizada em sistemas modernos e escaláveis, garantindo **resiliência**, **tolerância a falhas** e **melhor desempenho** em aplicações distribuídas.  

---

### Professor
- Luciano Camargo

### Alunos:
- Ricardo Rigo Antunes: RA: 1136661
- Jean Canova: RA: 1137244
- João Vitor Spiller: RA: 1137246