# 연구실 논문 작성 스타일 가이드

## 1. 전체 논문 구성

우리 연구실 논문은 보통 다음 흐름을 따른다.

1. Introduction
2. Related Work
3. Proposed Method / Materials and Methods
4. Experiments / Experimental Results
5. Discussion / Analysis
6. Conclusion

핵심 스타일은 문제 배경을 넓게 제시한 뒤, 기존 연구의 한계를 정리하고, 제안 방법의 구조와 실험적 검증을 체계적으로 보여주는 것이다.

## 2. Introduction 작성 방식

Introduction은 보통 다음 순서로 작성한다.

1. 연구 분야의 중요성과 실제 응용 배경을 설명한다.
2. 현재 문제 상황을 구체적으로 제시한다.
3. 기존 연구가 해결하지 못한 한계를 설명한다.
4. 그 한계 때문에 제안 방법이 필요한 이유를 연결한다.
5. 제안 방법의 핵심 아이디어를 간단히 소개한다.
6. 마지막에 contribution을 정리한다.

첫 문단은 너무 좁은 기술 설명으로 시작하지 않고, autonomous driving, agriculture, medical imaging, biometric recognition처럼 응용 분야의 중요성에서 시작하는 경향이 있다.

## 3. Related Work 작성 방식

Related Work는 기존 연구를 단순 나열하지 않고 카테고리로 나누어 설명한다.

자주 쓰는 분류 방식은 다음과 같다.

- 기존 방법이 특정 문제를 고려하는지 여부
- CNN 기반 방법과 Transformer 기반 방법
- single-scale 방법과 multi-scale 방법
- teacher-student 또는 knowledge distillation 적용 여부
- 기존 방법과 제안 방법의 차이

각 카테고리에서는 대표 연구의 장점을 설명한 뒤, 남아 있는 한계를 제시하고 제안 방법의 필요성으로 연결한다.

## 4. Proposed Method 작성 방식

Proposed Method는 전체 pipeline을 먼저 설명한 뒤 세부 모듈로 들어간다.

보통 포함하는 내용은 다음과 같다.

- 전체 framework 또는 workflow
- 입력 데이터와 출력 결과
- teacher network와 student network 구조
- proposed module의 목적
- attention, feature fusion, knowledge distillation, loss function 설명
- 각 모듈이 성능 향상에 기여하는 이유

첫 subsection은 대개 "Overall procedure", "Overall workflow", "Overview of the proposed method"처럼 전체 구조를 설명한다.

## 5. Experiments 작성 방식

Experiments 섹션에는 보통 다음 내용을 포함한다.

1. Dataset 설명
2. Train/validation/test split
3. Experimental setup
4. Training details
5. Evaluation metrics
6. SOTA method와 정량 비교
7. Ablation study
8. Computational complexity 또는 inference time
9. Qualitative result

우리 연구실 스타일에서는 실험 조건을 비교적 자세히 적고, 공정한 비교를 위해 동일한 split, 동일한 training condition, 동일한 metric을 사용했다는 점을 강조한다.

## 6. Discussion / Analysis 작성 방식

Discussion 또는 Analysis 섹션은 단순히 결과를 반복하지 않고, 왜 제안 방법이 효과적인지 해석하는 역할을 한다.

자주 포함되는 내용은 다음과 같다.

- Statistical analysis
- t-test와 Cohen's d-value
- Grad-CAM 또는 Grad-CAM++ 기반 시각화
- Class activation map 분석
- Difference image 또는 frequency-domain visualization
- Error case 분석
- Cross-domain robustness
- Domain shift 분석
- Computational cost 비교
- Limitations

Grad-CAM은 보통 Discussion 또는 Analysis 섹션에서 모델이 어떤 영역에 집중하는지 설명할 때 사용한다. 정량 성능만으로 부족한 설명을 보완하고, 제안 모듈이 의미 있는 feature를 학습했다는 근거로 활용한다.

## 7. 섹션별 작성 조언

Introduction을 쓸 때는 배경, 문제, 기존 한계, 제안 방법, contribution 순서로 작성한다.

Experiments를 쓸 때는 dataset, setup, metric, SOTA comparison, ablation study를 기본 구성으로 둔다.

Discussion을 쓸 때는 Grad-CAM, error case, statistical analysis, computational cost, limitation 중 논문 주제에 맞는 분석을 넣는다.

Grad-CAM은 단순 그림 제시가 아니라, 제안 방법이 baseline보다 더 적절한 영역에 집중한다는 해석과 함께 사용한다.

Ablation study는 제안한 모듈이 실제로 성능 향상에 기여하는지 보여주는 핵심 실험으로 넣는다.