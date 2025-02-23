# llm_service

LLM Service that touches upon core concepts learned in the past 5 years at Brex.

* [**Backend Knowledge for Microservices**]
  * [**Kotlin**] Learning to code in Kotlin, learning to utilize its native async functionalities 
  * [**Scaffolding**] Scaffolding Data Intensive Applications from Scratch Using Bazelisk. Deployment via Kubernetes K8s, deployed on AWS EC2
    * one-chart, Micronaut for JVM deployment (prior: helm + jsonnet based deployment envvar charts)
  * [**gRPC & Protobuf**] Exposing gRPC endpoints for internal microservices & external calls
  * [**Async/Event Driven**] Kafka topics for transactional event publishing, and async handling of external service's published events
    * handling common-case race condition issues, managing explosive complexities based on exponential nature of async infra's dependencies
  * [**GraphQL**] Wiring GraphQL endpoints to handle DGS calls from FE
  * [**ACID Transactional DB**] Postgres DB for real-time database READ & WRITE operations
  * [**Latency Optimizations**] Optimizations to decrease the latency of inference calls for gRPC via multi-threaded execution
  * [**Feature Flagging**] Feature Flags via various 3rd party systems (LaunchDarkly/Statsig). Experiments & incremental roll-outs
* [**ML Engineering**]
  * [**Pytorch**] Manipulating tensors, high dimensional matrix operations, BackProp, Forward, tensor math
  * [**Transformers**] Fine-tuning the Transformer Models using Pytorch and refined Datasets. HuggingFace
    * [**NLP**] BERT model fine-tuning. 
  * [**Data Manipulation**] Data Exploration (pandas, numpy, matplotlib, SQL) - anomaly detection, null value handling, plotting
  * [**ML Fundamentals**] (sklearn) Bias/Variance Tradeoff, Class Imbalance and SMOTE, T/P-tests & hypothesis testing, tree-based Classifiers & Regression models 
  * [**Deployment**] Deploying fine-tuned LLMs for inference using gRPCs/HTTPs



Setup
* Manual
```buildoutcfg
pip3 install -r requirements.txt --target=./deps
```

* Bazelisk
```buildoutcfg
bazelisk clean --expunge
bazelisk build //app:main --verbose_failures --explain=build.log
```