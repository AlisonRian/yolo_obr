# YOLO OBR - Detecção de Vítimas

Projeto de visão computacional utilizando **YOLOv8** para detecção e classificação de vítimas na arena de resgate da **OBR (Olimpíada Brasileira de Robótica)**.

---

## 🎯 Classes Detectadas

O modelo foi treinado para identificar duas classes de objetos:
* **`0: dead`** — Vítima morta (esfera prateada)
* **`1: alive`** — Vítima viva (esfera preta)

---

## 📁 Estrutura do Projeto

```text
yolo_obr/
├── data/
│   ├── train/       # Imagens e anotações de treino (~70%)
│   ├── val/         # Imagens e anotações de validação (~20%)
│   └── test/        # Imagens e anotações de teste (~10%)
├── detect/          # Resultados e pesos dos treinamentos realizados
│   └── train/weights/best.pt  # Melhor modelo salvo
├── data.yaml        # Configurações das pastas e classes do dataset
├── train.py         # Script para treinar o modelo
├── predict.py       # Script para inferência/teste com o modelo treinado
└── README.md
```

---

## 🚀 Como Executar

### 1. Instalar Dependências

Certifique-se de ter o Python 3.8+ instalado e instale a biblioteca da Ultralytics:

```bash
pip install ultralytics
```

### 2. Treinar o Modelo

Para iniciar o treinamento com o modelo base `yolov8n.pt`:

```bash
python train.py
```

*Os pesos finais e melhores resultados serão salvos em `detect/train/weights/`.*

### 3. Fazer Predições (Inferência)

Para rodar a detecção nas imagens da pasta de teste:

```bash
python predict.py
```

Os resultados anotados serão salvos na pasta de execuções do YOLO (`runs/detect/predict`).

---

## 📊 Desempenho do Modelo

Resultados obtidos no conjunto de validação após 100 épocas de treinamento:

* **mAP@50:** ~99.5%
* **mAP@50-95:** ~96.9%
* **Precisão:** ~99.8%
* **Recall:** 100%
