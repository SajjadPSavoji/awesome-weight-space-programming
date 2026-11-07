<div align="center">

# Awesome Weight-Space Programming [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Language models that read, edit and write the weights of other neural networks directly, without gradient descent.**

[![Last commit](https://img.shields.io/github/last-commit/SajjadPSavoji/awesome-weight-space-programming?color=green)](https://github.com/SajjadPSavoji/awesome-weight-space-programming/commits/main)
![Entries](https://img.shields.io/badge/entries-532-blue)
![Updated](https://img.shields.io/badge/updated-daily-orange)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

</div>

*Weight-space programming* was named in the MIT CSAIL report [Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) (2026-11-02). A general LLM is given another network's weights, sometimes with code and a budget of forward passes, and changes the numbers to explain, repair or build behavior. This list tracks the papers, code, benchmarks and critiques that follow, grouped by the kind of network being programmed. The [Foundations](#-foundations-weight-programming-before-wsp) section traces the eighty years of earlier work, from McCulloch and Pitts (1943) to 2025, that read, edited or wrote weights under other names. It is rebuilt from [`data/entries.json`](data/entries.json).

## 🔥 Recently Added

- **2026-11-07** · [Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility](https://arxiv.org/abs/2610.20139) (Interpretability)
- **2026-11-07** · [From Parameters to Behaviors: A Survey of Model Fusion for Large Language Models](https://arxiv.org/abs/2609.19553) (Model merging and weight arithmetic)
- **2026-11-07** · [Machine Unlearning for Large Language Models: Foundations, Advances, and Agentic Extensions](https://arxiv.org/abs/2609.30909) (Steering, representation engineering and unlearning)
- **2026-11-07** · [A Survey on the Linear Representation Hypothesis](https://arxiv.org/abs/2609.22695) (Interpretability)
- **2026-11-07** · [Open Technical Problems in Open-Weight AI Model Risk Management](https://arxiv.org/abs/2608.07514) (Backdoors and weight-level attacks)
- **2026-11-07** · [Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks](https://arxiv.org/abs/2607.07907) (Steering, representation engineering and unlearning)
- **2026-11-07** · [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) (LLMs as optimizers and self-improving agents)
- **2026-11-07** · [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) (LLMs as optimizers and self-improving agents)
- **2026-11-07** · [Position: The Term "Machine Unlearning" Is Overused in LLMs](https://arxiv.org/abs/2606.27379) (Steering, representation engineering and unlearning)
- **2026-11-07** · [Make Mechanistic Interpretability Auditable: A Call to Develop Guidelines via Continuous Collaborative Reviewing](https://arxiv.org/abs/2606.00033) (Interpretability)
- **2026-11-07** · [Large Language Models as Optimizers: A Survey of Direct vs. Tool-Augmented Approaches and Their Performance Frontiers](https://arxiv.org/abs/2606.15577) (LLMs as optimizers and self-improving agents)
- **2026-11-07** · [Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies](https://arxiv.org/abs/2606.23075) (LLMs as optimizers and self-improving agents)

## 🧭 Milestones

| Date | Milestone | Who | Work |
|:--|:--|:--|:--|
| 2026-11-02 | Term coined | MIT CSAIL | [Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/) |
| 2026-11-04 | First robot policies | Lingxiao Guo, Angchen Xie | [Astra weight edits on a VLA, a world action model and humanoid control](https://x.com/Lingxiao234/status/2118048171649806424) |
| 2026-11-05 | First Claude edit of a robot policy | Shanghai Innovation Institute, SJTU, HKU | [Opus 5.5 makes π0.5 move faster and smoother by editing its weights](https://cuzyoung.github.io/robotics-weight-editing/en/) |

## Contents

- [🌟 The Original Report](#-the-original-report) (1)
- [💬 Language Models](#-language-models) (6)
  - [Repairing behavior](#repairing-behavior) (3)
  - [Reading and predicting from weights](#reading-and-predicting-from-weights) (2)
  - [Writing networks from scratch](#writing-networks-from-scratch) (1)
- [🦾 Robotics and Control](#-robotics-and-control) (10)
  - [Vision-language-action models](#vision-language-action-models) (3)
  - [RL control policies](#rl-control-policies) (7)
- [🧩 Other Domains](#-other-domains) (7)
- [🎮 Games](#-games) (5)
- [📊 Benchmarks and Evaluations](#-benchmarks-and-evaluations) (2)
- [🛠️ Tools, Harnesses and Agent Skills](#-tools-harnesses-and-agent-skills) (9)
- [🔍 Analyses and Critiques](#-analyses-and-critiques) (9)
- [📜 Foundations: Weight Programming Before WSP](#-foundations-weight-programming-before-wsp) (188)
  - [Hand-set and compiled weights](#hand-set-and-compiled-weights) (16)
  - [Rule insertion and extraction](#rule-insertion-and-extraction) (12)
  - [Weight surgery and pruning](#weight-surgery-and-pruning) (13)
  - [Fast weights and self-modifying networks](#fast-weights-and-self-modifying-networks) (11)
  - [Neuroevolution and gradient-free weight search](#neuroevolution-and-gradient-free-weight-search) (12)
  - [Hypernetworks and weight generation](#hypernetworks-and-weight-generation) (12)
  - [Model editing](#model-editing) (13)
  - [Weight arithmetic and merging](#weight-arithmetic-and-merging) (13)
  - [Weight-space learning](#weight-space-learning) (13)
  - [Mechanistic interpretability that reads weights](#mechanistic-interpretability-that-reads-weights) (13)
  - [Activation steering](#activation-steering) (3)
  - [Automated interpretability agents](#automated-interpretability-agents) (11)
  - [Language-to-weights and LLM program search](#language-to-weights-and-llm-program-search) (12)
  - [Weight-level security and safety](#weight-level-security-and-safety) (12)
  - [Policy surgery, control and robot policies](#policy-surgery-control-and-robot-policies) (22)
- [📖 Surveys and Reviews](#-surveys-and-reviews) (295)
  - [Model and knowledge editing](#model-and-knowledge-editing) (24)
  - [Model merging and weight arithmetic](#model-merging-and-weight-arithmetic) (13)
  - [Steering, representation engineering and unlearning](#steering-representation-engineering-and-unlearning) (30)
  - [Interpretability](#interpretability) (62)
  - [Rule extraction and neural-symbolic integration](#rule-extraction-and-neural-symbolic-integration) (30)
  - [Weight-space learning, parameter generation and hypernetworks](#weight-space-learning-parameter-generation-and-hypernetworks) (8)
  - [Meta-learning, learned optimizers and fast weights](#meta-learning-learned-optimizers-and-fast-weights) (14)
  - [Neuroevolution and gradient-free search](#neuroevolution-and-gradient-free-search) (17)
  - [Pruning and compression](#pruning-and-compression) (20)
  - [Backdoors and weight-level attacks](#backdoors-and-weight-level-attacks) (30)
  - [LLMs as optimizers and self-improving agents](#llms-as-optimizers-and-self-improving-agents) (32)
  - [Verification and policy reuse](#verification-and-policy-reuse) (15)
- [Legend](#legend)
- [How This List Is Maintained](#how-this-list-is-maintained)
- [Related Lists](#related-lists)
- [Contributing](#contributing)
- [Citation](#citation)

## 🌟 The Original Report

*Where the term comes from.*

- **[Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights](https://rikiyat.github.io/blog/weight-space-programming/)**  
  MIT CSAIL · *Blog report* · 2026-11-02 · `💻 code / results`  
  [[Post](https://rikiyat.github.io/blog/weight-space-programming/)] [[Thread](https://x.com/rikiyatakehi/status/2117313742891327994)] [[Code](https://github.com/RikiyaT/lm_understand-logs)] ![GitHub stars](https://img.shields.io/github/stars/RikiyaT/lm_understand-logs?style=social)  
  GPT-6 Astra names what networks were trained on from their weights alone, repairs a stuck Kinetix car policy (0% to 100%, 3.5% of weights, one reply, no tools), writes MinAtar and 9x9 Go networks from zero, and lifts Qwen3.5-0.8B on MATH-500 from 7.9% to 48.1% by removing a loop direction (0.016% of weights). Edits removed a blocker; they did not add a missing ability (Gemma 3 270M: no gain).

## 💬 Language Models

*Reading, repairing and writing the weights of language models.*

### Repairing behavior

- **[fderrigo/weight-space-programming-experiments](https://github.com/fderrigo/weight-space-programming-experiments)**  
  Filippo Derrigo · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/fderrigo/weight-space-programming-experiments)] ![GitHub stars](https://img.shields.io/github/stars/fderrigo/weight-space-programming-experiments?style=social)  
  Code, patches and results for two no-training edits chosen by Codex. Qwen2.5-0.5B-Instruct Pinocchio fix changed 8.868% of values: target answers 0/24 to 11/24, with 7/8 original controls preserved. Qwen3-0.6B patch raised unauthorized tool calls on target requests from 1/40 to 13/40; selectivity incomplete.

- **[weights_editing: replicating Sparks of Weight-Space Programming across LLMs](https://github.com/alan-turing-institute/weights_editing)**  
  The Alan Turing Institute · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/alan-turing-institute/weights_editing)] ![GitHub stars](https://img.shields.io/github/stars/alan-turing-institute/weights_editing?style=social)  
  Replicates the weight-editing experiments with several LLMs as the editor. The repository returned 404 on 2026-11-05.

- **[OpenWSP](https://github.com/openwsp/openwsp)**  
  OpenWSP · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/openwsp/openwsp)] ![GitHub stars](https://img.shields.io/github/stars/openwsp/openwsp?style=social)  
  An open replication with a Python kernel over weights, a forward-pass service and a versioned edit format (CLI, SDK and MCP server). Its own one-shot GPT-6 Astra rerun of the car repair failed (0/1,024, 2,918 weights changed).

### Reading and predicting from weights

- **[Can GPT-6 Astra read and write GPT-2's weights?](https://github.com/AlexBodner/wsp-scaling)**  
  Alex Bodner · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/AlexBodner/wsp-scaling)] ![GitHub stars](https://img.shields.io/github/stars/AlexBodner/wsp-scaling?style=social)  
  Asks GPT-6 Astra to find induction heads in scrambled GPT-2 small (124M) weights. With Python and no hint it picked all five induction heads in both runs (10 of 10 picks); with no tools, 0 of 10. Silencing the five heads cuts repeat accuracy from 98.6% to 28.9%. One model, few runs, no size sweep.

- **[Weight-space programming autoresearch](https://github.com/csinva/weight-space-programming-autoresearch)**  
  csinva · *GitHub* · 2026-11 · `💻 code / results`  
  [[Code](https://github.com/csinva/weight-space-programming-autoresearch)] ![GitHub stars](https://img.shields.io/github/stars/csinva/weight-space-programming-autoresearch?style=social)  
  Claude, running as a coding agent, hand-writes transformer weights: 959 programs, and all 10 algorithmic tasks reach 100% within three attempts. A second test is mostly negative: Claude Opus 5.5 reading Qwen3.5-0.8B weights predicts the effects of 420 edits only slightly better than without the numbers (+0.06 correlation).

### Writing networks from scratch

- **[allthingssecurity/weight_space_programming](https://github.com/allthingssecurity/weight_space_programming)**  
  allthingssecurity · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/allthingssecurity/weight_space_programming)] ![GitHub stars](https://img.shields.io/github/stars/allthingssecurity/weight_space_programming?style=social)  
  Writes parameters of a randomly initialized model with the Qwen3.5-0.8B architecture directly, without gradient descent, to answer ABAP questions. Reports 18/25 correct in a small, unblinded static review, with random controls at 0/25. Includes 7 supplied-answer recall cases; not an expert ABAP model.

## 🦾 Robotics and Control

*Weight edits on robot policies, VLAs, world action models and controllers.*

### Vision-language-action models

- **[Opus 5.5 makes π0.5 move faster and smoother by editing its weights](https://cuzyoung.github.io/robotics-weight-editing/en/)**  
  Shanghai Innovation Institute, SJTU, HKU · *Project page* · 2026-11-05 · `💬 post only`  
  [[Post](https://cuzyoung.github.io/robotics-weight-editing/en/)] [[Code](https://github.com/Cuzyoung/robotics-weight-editing)]  
  Claude Opus 5.5, working in Claude Code from recorded rollouts, changed 1.16% of a Training-Time-RTC π0.5 for a real YAM bimanual robot. Bottle placement got 12.0% faster at 40 Hz and jumps between action chunks fell 89.8%; both policies kept 100% success (3 runs per condition). The edits were a RoPE intervention fitted into Q/K weights by least squares and a repair of a prefix-handling bug in official RTC. Project page only, no code or weights.

- **[Astra weight edits on a VLA, a world action model and humanoid control](https://x.com/Lingxiao234/status/2118048171649806424)**  
  Lingxiao Guo, Angchen Xie · *X thread* · 2026-11-04 · `💬 post only`  
  [[Thread](https://x.com/Lingxiao234/status/2118048171649806424)]  
  π0.5 on 5 RoboTwin 2.0 tasks: 27% to 65% with about 4 edits on held-out episodes; on one task 4 of 3.6B parameters took success from 28/92 to 82/92. FastWAM gains 8.7 points. Unitree G1 policies adapt to a hidden payload by rewiring waist and knee gains. Candidates are found by probing saved inputs offline, then checked with rollouts. Each edited π0.5 was fine-tuned on one task, so gains hold for that task only; no code or paper as of 2026-11-05.

- **[Weight-Space Programming for VLAs](https://github.com/Geeksongs/Weight-Space-Programming-VLA)**  
  Geeksongs · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/Geeksongs/Weight-Space-Programming-VLA)] [[Model](https://huggingface.co/pythonsong/smolvla-libero-wsp-B35)] ![GitHub stars](https://img.shields.io/github/stars/Geeksongs/Weight-Space-Programming-VLA?style=social)  
  Changing one number in SmolVLA (the x-action output bias) lifts a LIBERO-Spatial task from 42/100 to 64/100 on unseen initial states (Fisher p = 0.003). The fault was read off rollouts: the gripper closed too far along x and regrasped.

### RL control policies

- **[wsp-lab: cross-editor stress test of weight-space programming](https://github.com/WKJBryan/wsp-lab)**  
  WKJBryan · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/WKJBryan/wsp-lab)] ![GitHub stars](https://img.shields.io/github/stars/WKJBryan/wsp-lab?style=social)  
  An agentic GLM-5.3 editor repaired a CartPole MLP from 9.4 to 371.6 return, while a matched-norm random edit scored 9.5. Pre-registered, with an untouched baseline and a retraining upper bound; a blind Qwen3.5-0.8B repair gave no gain.

- **[Admiral: Muse Spark repairs a multi-agent RL policy by editing its weights](https://github.com/faresboudelaa/admiral)**  
  Fares Boudelaa · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/faresboudelaa/admiral)] ![GitHub stars](https://img.shields.io/github/stars/faresboudelaa/admiral?style=social)  
  Meta Muse Spark built a gated "steer home" circuit in a 163,874-parameter MAPPO capture-the-flag boat policy (PyQuaticus), changing 2.9% of weights. Against the hard heuristic opponent, paired score rose +0.36 over 200 held-out matches; against medium, +0.01 (not significant). Ships a reusable sandboxed numpy kernel with a match budget and a no-training audit.

- **[Quadrotor PPO under actuation delay: LLM weight edits vs a gain sweep](https://github.com/filippos-p/drone-ppo-delay-robustness)**  
  filippos-p · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/filippos-p/drone-ppo-delay-robustness)] ![GitHub stars](https://img.shields.io/github/stars/filippos-p/drone-ppo-delay-robustness?style=social)  
  Two LLMs each made one blind edit to a PyBullet quadrotor policy. At 4 ms delay the original succeeds 5%, the LLM edits 16% and 12%, a 28-variant output-gain sweep 67% and retraining for 7M steps 61%; at 8 ms or more the LLM edits score 0–1%. A clear case of a scripted baseline beating the LLM edit.

- **[Weight-space programming for F1TENTH autonomous racing](https://github.com/Ro0t-set/f1tenth-weight-space-racing)**  
  Ro0t-set · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/Ro0t-set/f1tenth-weight-space-racing)] ![GitHub stars](https://img.shields.io/github/stars/Ro0t-set/f1tenth-weight-space-racing?style=social)  
  GPT-6 Astra edited 1,276 scalars of a PPO LiDAR racing controller: completions went from 167 to 180 of 210 paired starts and crashes from 43 to 30. Runnable with a lock file and checkpoints.

- **[Reproducing Sparks of Weight-Space Programming with Claude Opus 5.5](https://github.com/EphraiemSarabamoun/weight-space-programming-opus)**  
  Ephraiem Sarabamoun · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/EphraiemSarabamoun/weight-space-programming-opus)] ![GitHub stars](https://img.shields.io/github/stars/EphraiemSarabamoun/weight-space-programming-opus?style=social)  
  Claude Opus 5.5 repeats the Kinetix car repair at 1,024/1,024 episodes, changing 1.70% of weights, along with other experiments from the report.

- **[Replication of Sparks of Weight-Space Programming with Claude Fable 5.1](https://github.com/Ludvik1kul/weight-space-programming-replication)**  
  Ludvik1kul · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/Ludvik1kul/weight-space-programming-replication)] ![GitHub stars](https://img.shields.io/github/stars/Ludvik1kul/weight-space-programming-replication?style=social)  
  Claude Fable 5.1 repeats the Kinetix car repair at 1,024/1,024 episodes, changing 2.16% of weights, and the MinAtar experiments.

- **[Policy Surgery](https://github.com/latentpaths/policy-surgery)**  
  latentpaths · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/latentpaths/policy-surgery)] [[Project](https://www.latentpaths.com/projects/policy-surgery)] ![GitHub stars](https://img.shields.io/github/stars/latentpaths/policy-surgery?style=social)  
  GPT-OSS-120B edits a 4,996-parameter LunarLander PPO actor after its dynamics change. Reversed thrusters: 0 to 226 of 256 held-out episodes. Crosswind and reduced thrust gain 3 to 6 points, and only one of those intervals excludes zero. Separate selection, approval and test seeds, with every failure kept.

## 🧩 Other Domains

*Classifiers, small decision networks and anything else.*

- **[sachgaur/WSP](https://github.com/sachgaur/WSP)**  
  sachgaur · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/sachgaur/WSP)] ![GitHub stars](https://img.shields.io/github/stars/sachgaur/WSP?style=social)  
  LeNet/MNIST pilot testing whether an agent can diagnose a failure from bounded numerical queries and repair it by editing the final classifier without training. Paired comparison of Astra and DeepSeek editors on fault and shortcut cases over seeds 42, 43 and 44, with a protocol fixed before evaluation.

- **[WeightLoop: Weight-Space Programming with Experimental Feedback](https://arxiv.org/abs/2611.07319)**  
  Mengran Li, Bo Li, Weijing Zhao, Chengyang Zhang, et al. · *Preprint* · 2026-11-05 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.07319)]  
  Framework in which GPT-6 Astra reads a task specification and model implementation, then writes a bounded parameter-editing program. The program turns experimental feedback into edits to a deployed predictor, with no further LLM calls or gradient retraining. In offline replay, targeted edits improve mean ranking utility in seven of eight endpoint-budget settings.

- **[Weight-Space Programming on Qwen3-ASR-0.6B: Nine Independent Agent Edits, Random-Direction Controls, and a Missing Attention Mask](https://doi.org/10.5281/zenodo.23976684)**  
  Taha Enes Aslantürk · *Zenodo preprint* · 2026-11-05 · `📝 preprint`  
  [[Paper](https://doi.org/10.5281/zenodo.23976684)] [[Code](https://huggingface.co/tahaenesaslanturk/Qwen3-ASR-0.6B-weight-space-programming)]  
  Applied the Sparks repair protocol to speech recognition. Nine Claude agent edits each reduced a silence-induced language-tagging failure, and the real edit beat matched random-direction controls in 26 of 27 comparisons. The failure turned out to be largely a missing attention mask in the inference backend, which the edits compensated for in weight space.

- **[Weight-Space Programming for the Social Safety Net](https://github.com/ctrimm/weight-space-programming)**  
  ctrimm · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/ctrimm/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/ctrimm/weight-space-programming?style=social)  
  Tests whether an LLM can write, with no training, the exact weights of small networks computing four simplified US benefit formulas (SNAP, EITC, SSI, Medicaid). Three of four match the formula to within a trillionth of a dollar; the EITC network differs at one point by 2.4 cents. Trained networks are off by dollars.

- **[Weight-space programming on a clinical splicing model](https://github.com/KristinaMruts/weight-space-programming-spliceai)**  
  KristinaMruts · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/KristinaMruts/weight-space-programming-spliceai)] ![GitHub stars](https://img.shields.io/github/stars/KristinaMruts/weight-space-programming-spliceai?style=social)  
  Claude Opus 5.5 hand-edits 165 weights of OpenSpliceAI-MANE-10000nt to separate pathogenic from benign ClinVar variants. Hidden-test AUPRC 0.9385 → 0.9746. A temperature-only control gives 0.9695 and gradient fine-tuning of the same layers 0.9697-0.9710; authors conclude the edit matched ordinary training rather than beating it.

- **[devichand579/gepa_wsp](https://github.com/devichand579/gepa_wsp)**  
  devichand579 · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/devichand579/gepa_wsp)] ![GitHub stars](https://img.shields.io/github/stars/devichand579/gepa_wsp?style=social)  
  Reflective GEPA loop in which LLMs (DeepSeek, MiniMax, Nemotron) propose weight edits for MNIST, Fashion-MNIST, SST-2 and diffusion networks, with no parameter-gradient updates. 45 retained trajectories, 3 seeds, 60 mutations, compared to Adam. It improves one-shot statistical weight programs but does not generally replace Adam.

- **[Weight-space programming for auditing clinical decision networks](https://arxiv.org/abs/2611.05341)**  
  Henry Ford Health · *Preprint* · 2026-11-03 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.05341)] ![GitHub stars](https://img.shields.io/github/stars/hnusrat1/weightspace-rt?style=social)  
  Claude Opus 5.5 audited small head-and-neck planning-request screening networks (433 to 4,801 parameters) blind, without tools, data or code execution. It named the broken rule in 16 of 18 flawed networks and repaired each of the 16 by changing a median of 3 parameters. Checks used about 420,000 requests.

## 🎮 Games

*Weight programming of game-playing networks and board-game policies.*

- **[mraad/weight-space-programming](https://github.com/mraad/weight-space-programming)**  
  mraad · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/mraad/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/mraad/weight-space-programming?style=social)  
  Replicates Weight-Space Programming on Claude with no training. Claude names Breakout from raw weights (correct, 93% confidence; 60% with W1 rows shuffled). A Claude-written Breakout network scores 269.4 ± 7.4 (PPO 500M: 25.3, GPT-6 Astra: 517.4). In the Three Pads lander game, each Claude-written 484-weight network lands 3,000 of 3,000 flights.

- **[Writing neural-network weights for Geister without training](https://github.com/nishio/geister-weight-space-programming)**  
  NISHIO Hirokazu · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/nishio/geister-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/nishio/geister-weight-space-programming?style=social)  
  Claude Opus 5.5 agents write, read and fix neural-network weights for Geister, a two-player hidden-information game, without training. Compared with PPO and text-prompted small LMs, on an 8-core CPU machine. Repository includes per-item results (G1-G26), writer and reader run transcripts, audits, and an English summary and Japanese report.

- **[Claude Fable 5.1 writes a Breakout network from scratch](https://github.com/niqbal/fable-weight-space-breakout)**  
  niqbal · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/niqbal/fable-weight-space-breakout)] ![GitHub stars](https://img.shields.io/github/stars/niqbal/fable-weight-space-breakout?style=social)  
  Fable 5.1 writes all 20,486 weights of a MinAtar Breakout policy in one reply and scores 501.6 ± 5.8, against 517.4 for Astra in the report.

- **[Weight-space MinAtar: Opus 5.5 and Fable 5.1 write game policies](https://github.com/Barneyjm/weight-space-minatar)**  
  Barneyjm · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/Barneyjm/weight-space-minatar)] ![GitHub stars](https://img.shields.io/github/stars/Barneyjm/weight-space-minatar?style=social)  
  Blind one-shot weight writing for MinAtar Breakout, Asterix and Seaquest. On Breakout, Fable 5.1 scores 533.9 and Opus 5.5 scores 7.1.

- **[Weight-space Breakout pipeline and FailureIsAllYouNeed](https://github.com/HarleyCoops/weight-space-breakout-pipeline)**  
  Christian (Harley) Cooper · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/HarleyCoops/weight-space-breakout-pipeline)] [[Model](https://huggingface.co/HarleyCooper)] ![GitHub stars](https://img.shields.io/github/stars/HarleyCoops/weight-space-breakout-pipeline?style=social)  
  A hosted Qwen editor repairs injected faults in a 17,253-parameter Breakout policy behind a verifier gate, publishing accepted weights to Hugging Face. A useful negative result: the one accepted repair just restored the known reference policy, one run made 123 turns without submitting an edit, and a later qualified repair improved sampled play while greedy return fell from 10.25 to 1.57. Follow-up repo: FailureIsAllYouNeed.

## 📊 Benchmarks and Evaluations

*Controlled tests of whether weight access helps.*

- **[Consistency Is Not Understanding: Orbit Audits for Neural Field Weight Readers](https://arxiv.org/abs/2611.05798)**  
  Sungguk Cha, Mintae Kim, Youngsub Han, Byoung-Ki Jeon, Sangyeob Lee · *Preprint* · 2026-11-04 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.05798)]  
  Tests whether readers recognize what shallow ReLU neural fields encode from their weights (480 shape fields, 1,000 MNIST fields), using hidden-neuron permutations and positive rescalings that leave the function unchanged. Compares statistics, set and language-model readers, with 1,920 scored reasoning-model sessions, and separates accuracy, agreement across transformed copies and disagreement on fresh identical prompts.

- **[WSPBench](https://github.com/alexcarterhq/wspbench)**  
  alexcarterhq · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/alexcarterhq/wspbench)] [[Project](https://wspbench.com)] ![GitHub stars](https://img.shields.io/github/stars/alexcarterhq/wspbench?style=social)  
  Does weight access help an agent diagnose and repair a model? GPT-6.1 Sol repaired 30/32 faults with behavior probes plus weights, against 14/32 with probes alone and 5/32 for a scripted solver at the same probe budget. All three kept 8 clean controls intact.

## 🛠️ Tools, Harnesses and Agent Skills

*Libraries and agent skills for reading and editing weights.*

- **[IyadhKhalfallah/weight-space-programming](https://github.com/IyadhKhalfallah/weight-space-programming)**  
  IyadhKhalfallah · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/IyadhKhalfallah/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/IyadhKhalfallah/weight-space-programming?style=social)  
  Experiments editing and writing models without gradient descent, plus a wsl CLI that applies reversible weight patches with per-slice regression checks. A hand-written XGBoost model reached AUC 0.809 on rain forecasting with zero labels (0.839 when trained on 2.5 years). On a 0.8B LLM, the author's edit did not reproduce the published effect.

- **[Weight-Space Programming (wsp-kit)](https://github.com/AuremHQ/weight-space-programming)**  
  Aurem · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/AuremHQ/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/AuremHQ/weight-space-programming?style=social)  
  Tool that tries to fix small open-weight models by editing weights directly, with an eval gate deciding whether an edit ships. Reports its own CPU runs on Qwen3-0.6B and GPT2-124M: in 60-item list-looping tests no edit passed the gate, so 0 weights shipped. Only the smoke-test pipeline passed (failing score 64.14 → 75.43).

- **[weightspace](https://github.com/leofmarciano/weightspace)**  
  Leo Marciano · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/leofmarciano/weightspace)] ![GitHub stars](https://img.shields.io/github/stars/leofmarciano/weightspace?style=social)  
  Apache-2.0 Python library: read, fix, write and improve any torch.nn.Module with an LLM, using budgeted probes, tracked edits and sparse patches. Its own rerun of the Qwen experiment did not beat the original edit.

- **[weight-space-programming-skill](https://github.com/di37/weight-space-programming-skill)**  
  di37 · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/di37/weight-space-programming-skill)] ![GitHub stars](https://img.shields.io/github/stars/di37/weight-space-programming-skill?style=social)  
  Claude Code skill for improving a small open LLM by editing its weights directly, with no training.

- **[weights-lab](https://github.com/oumi-ai/weights-lab)**  
  Oumi · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/oumi-ai/weights-lab)] ![GitHub stars](https://img.shields.io/github/stars/oumi-ai/weights-lab?style=social)  
  Agent skill for editing LLM weights.

- **[pi-weight-space-programming](https://github.com/felipepenha/pi-weight-space-programming)**  
  Felipe Penha · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/felipepenha/pi-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/felipepenha/pi-weight-space-programming?style=social)  
  Extension for the Pi coding agent with skills for reading and editing weights.

- **[OpenWiSH: Open Weight-Space Harness](https://github.com/Alexander-Aghili/OpenWiSH)**  
  Alexander Aghili · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/Alexander-Aghili/OpenWiSH)] ![GitHub stars](https://img.shields.io/github/stars/Alexander-Aghili/OpenWiSH?style=social)  
  An agent-agnostic harness (claude -p, Codex or the Anthropic API) where agents inspect and edit weights through a Rust edit gate. Already runs Kinetix and MinAtar tasks.

- **[weight-surgery](https://github.com/lorenzofamiglini/weight-surgery)**  
  Lorenzo Famiglini · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/lorenzofamiglini/weight-surgery)] ![GitHub stars](https://img.shields.io/github/stars/lorenzofamiglini/weight-surgery?style=social)  
  Open agent skill that reads weights first, keeps a fixed forward-pass budget and proves fixes on held-out data. On a BERT NER model, a fitted control beat the hand edit (+0.109 vs +0.032 F1).

- **[weight-space-programming (agent skill)](https://github.com/xero00000/weight-space-programming)**  
  xero00000 · *GitHub* · 2026-11-02 · `💻 code / results`  
  [[Code](https://github.com/xero00000/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/xero00000/weight-space-programming?style=social)  
  Agent skill for reasoning-driven weight inspection, targeted edits and small-network construction.

## 🔍 Analyses and Critiques

*Audits, replications of claims and critical takes.*

- **[Does Claude have it too? Replicating 'Sparks of Weight-Space Programming'](https://github.com/dhaneshnm/wsp-replication)**  
  dhaneshnm · *GitHub* · 2026-11-06 · `💻 code / results`  
  [[Code](https://github.com/dhaneshnm/wsp-replication)] ![GitHub stars](https://img.shields.io/github/stars/dhaneshnm/wsp-replication?style=social)  
  Replication of the MinAtar write-from-scratch experiment with Claude Opus 5.5, using the same prompts and scorer. In each game one of three one-shot replies reached 87%, 97% and 86% of GPT-6 Astra's score; median replies reached 51%, 14% and 62%. Claude beats PPO at 100M steps in every game.

- **[Rethinking Weight-Space Programming](https://github.com/ZhangYiqun018/rethinking-weight-space-programming)**  
  Yiqun Zhang · *GitHub* · 2026-11-05 · `💻 code / results`  
  [[Code](https://github.com/ZhangYiqun018/rethinking-weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/ZhangYiqun018/rethinking-weight-space-programming?style=social)  
  Re-runs the report's experiments with baselines and controls. Tuned PPO reaches 99.2–114.4 on Seaquest vs Astra's 53.1. Unedited Qwen3.5-0.8B with thinking off scores 44.2% on MATH-500. A difference-of-means direction with no LLM reaches 41.9%. Without simulator source in the prompt, Seaquest median falls to 0.8.

- **[Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"](https://arxiv.org/abs/2611.08070)**  
  Nazmus Sakib Ahmed · *Preprint* · 2026-11-05 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.08070)]  
  Tests Claude Opus 5.5 reading raw weights, given as plain text without tools, of ~125,000-parameter CNNs trained on five image datasets. Finds accurate local arithmetic but reliance on dataset priors: with CIFAR-10 labels permuted, every class pair the model interprets is wrong. Exploratory, mostly single runs; provides an auditing protocol.

- **[Weight-space horizon: re-evaluating the released MinAtar networks](https://github.com/hamley241/weight-space-horizon)**  
  hamley241 · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/hamley241/weight-space-horizon)] ![GitHub stars](https://img.shields.io/github/stars/hamley241/weight-space-horizon?style=social)  
  A pre-registered re-evaluation finds 51.6% of the released Breakout episodes still running at the 10K-step cap; a 30K cap adds 405.3 reward. Episode caps are a way to misread WSP scores.

- **[The 'Astra can read and write weights to improve Qwen' post is misleading](https://honnibal.dev/blog/astra-read-write-misleading)**  
  Matthew Honnibal · *Blog* · 2026-11-03 · `💬 post only`  
  [[Post](https://honnibal.dev/blog/astra-read-write-misleading)]  
  Separates reading weights directly from repairing a model with code and practice feedback: raw-weight reading without tools appears only on the smallest networks, and the language-model results used Python and forward passes.

- **[MIT team says GPT-6 Astra can improve other AI models by editing their weights. Critics say its biggest result relied on standard ML engineering.](https://www.rdworldonline.com/mit-team-says-gpt-6-astra-can-fix-an-ai-model-by-editing-its-weights-critics-say-the-method-was-standard-ml-engineering/)**  
  R&D World · *News* · 2026-11-03 · `💬 post only`  
  [[Post](https://www.rdworldonline.com/mit-team-says-gpt-6-astra-can-fix-an-ai-model-by-editing-its-weights-critics-say-the-method-was-standard-ml-engineering/)]  
  News coverage of the claims and the methodological pushback.

- **[Sparks of Weight-Space Programming — Complete Reproduction & Interactive Guide (EN / KO)](https://github.com/statsleelab/weight_space_programming)**  
  statsleelab · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Code](https://github.com/statsleelab/weight_space_programming)] [[Project](https://statsleelab.github.io/weight_space_programming/)] ![GitHub stars](https://img.shields.io/github/stars/statsleelab/weight_space_programming?style=social)  
  Reproduction of all 8 experiments of the MIT report from the released weights, prompts and logs, with standalone NumPy/SciPy verification scripts. Reports max tensor difference 0.0 and a full run of about 3.5 seconds on CPU. Includes a bilingual (English/Korean) interactive web report and a separate Drosophila connectome weight-edit page.

- **[Flecart/weight-programming](https://flecart.github.io/posts/2026-11-03-i-tried-to-break-weight-programming/)**  
  Xuanqiang Angelo Huang · *GitHub* · 2026-11-03 · `💻 code / results`  
  [[Post](https://flecart.github.io/posts/2026-11-03-i-tried-to-break-weight-programming/)] [[Code](https://github.com/Flecart/weight-programming)] ![GitHub stars](https://img.shields.io/github/stars/Flecart/weight-programming?style=social)  
  Replication and stress tests of 'Sparks of Weight Space Programming'. Hand-written MinAtar networks match published scores; the Kinetix car fix succeeds in 1,024/1,024 episodes. A Breakout network scores 517 versus 534 for a Python script with the same algorithm. Tests obfuscation (156/156 correct) and Claude Opus 5.5 writing networks.

- **[The Mathematics of Weight-Space Programming](https://doi.org/10.5281/zenodo.23933590)**  
  Miquel Noguer Alonso · *Zenodo preprint* · 2026-11-03 · `📝 preprint`  
  [[Paper](https://doi.org/10.5281/zenodo.23933590)]  
  Gives conditions under which a selective edit to a transformer's final feed-forward module is possible, minimum-cost edits under explicit preservation constraints, and certificates of infeasibility. The editors are explicit algorithms, not LLMs; on GPT-2 CounterFact edits, interval constraints improved neighbor retention by about 20 points.

## 📜 Foundations: Weight Programming Before WSP

*Eighty years of work that read, edited or wrote network weights under other names, oldest first, in fourteen lineages; plus recent related work that does not use a language model as the editor.*

### Hand-set and compiled weights

- **[A logical calculus of the ideas immanent in nervous activity](https://doi.org/10.1007/BF02478259)**  
  U. Illinois College of Medicine / U. Chicago · *Bulletin of Mathematical Biophysics* · 1943 · `📄 peer-reviewed` · 18.6k citations (OA)  
  [[Paper](https://doi.org/10.1007/BF02478259)]  
  Proves that nets of threshold units with hand-chosen excitatory and inhibitory connections can realise any finite logical expression: the first networks whose weights are programmed by hand.

- **[Representation of events in nerve nets and finite automata](https://doi.org/10.1515/9781400882618-002)**  
  S.C. Kleene · *Automata Studies, Princeton UP* · 1956 · `📄 peer-reviewed` · 2k citations (S2)  
  [[Paper](https://doi.org/10.1515/9781400882618-002)]  
  Proves that nets of threshold units are equivalent to finite automata and introduces regular expressions, the theoretical root of compiling automata into networks.

- **[Non-Holographic Associative Memory](https://doi.org/10.1038/222960a0)**  
  D. J. Willshaw, O. P. Buneman, H. C. Longuet-Higgins · *Nature* · 1969 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://doi.org/10.1038/222960a0)]  
  Introduces a clipped outer-product associative memory whose connection matrix is written in one shot from the patterns to be stored, following Hebb's correlation rule.

- **[Correlation Matrix Memories](https://doi.org/10.1109/TC.1972.5008975)**  
  Teuvo Kohonen · *IEEE Transactions on Computers* · 1972 · `📄 peer-reviewed` · 1k citations (S2)  
  [[Paper](https://doi.org/10.1109/TC.1972.5008975)]  
  Presents a correlation-matrix memory whose matrix is written in one shot as a sum of outer products of the patterns to be stored.

- **[Neural networks and physical systems with emergent collective computational abilities](https://doi.org/10.1073/pnas.79.8.2554)**  
  Caltech / Bell Laboratories · *PNAS* · 1982 · `📄 peer-reviewed` · 20.5k citations (S2)  
  [[Paper](https://doi.org/10.1073/pnas.79.8.2554)]  
  Writes the weights of a symmetric recurrent network in one pass with the outer-product rule T_ij = Σ_s (2V_i^s−1)(2V_j^s−1) over the stored patterns, with no training.

- **[Neural" computation of decisions in optimization problems](https://doi.org/10.1007/BF00339943)**  
  Caltech / AT&T Bell Laboratories · *Biological Cybernetics* · 1985 · `📄 peer-reviewed` · 3.4k citations (S2)  
  [[Paper](https://doi.org/10.1007/BF00339943)]  
  Derives a continuous Hopfield network's weights analytically from an energy function that encodes the Travelling Salesman Problem, with no learning. Moves from storing memories to compiling a task into the network.

- **[Collective computational properties of neural networks: New learning mechanisms](https://doi.org/10.1103/PhysRevA.34.4217)**  
  ESPCI Paris · *Physical Review A* · 1986 · `📄 peer-reviewed` · 325 citations (S2)  
  [[Paper](https://doi.org/10.1103/PhysRevA.34.4217)]  
  Gives a closed-form pseudo-inverse rule, W = X X⁺, that computes the weights of an associative network directly from the patterns to be stored.

- **[On the computational power of neural nets](https://doi.org/10.1006/jcss.1995.1013)**  
  Rutgers University · *J. Computer and System Sciences* · 1995 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://doi.org/10.1006/jcss.1995.1013)]  
  Proves, by explicit weight construction, that a finite recurrent network with rational weights simulates any Turing machine. Appeared at COLT 1992 and in the Journal of Computer and System Sciences in 1995.

- **[A neural compiler](https://doi.org/10.1016/0304-3975(94)00200-3)**  
  LIP, ENS Lyon; CEA Grenoble · *Theoretical Computer Science* · 1995 · `📄 peer-reviewed` · 45 citations (S2)  
  [[Paper](https://doi.org/10.1016/0304-3975(94)00200-3)]  
  Presents a neural compiler that translates programs in a high-level, Pascal-like language into networks whose weights and topology are fully determined by the program.

- **[Constructing deterministic finite-state automata in recurrent neural networks](https://doi.org/10.1145/235809.235811)**  
  NEC Research Institute / RPI · *Journal of the ACM* · 1996 · `📄 peer-reviewed` · 210 citations (S2)  
  [[Paper](https://doi.org/10.1145/235809.235811)]  
  Gives a provably stable way to program a second-order recurrent network so that it implements any given deterministic finite-state automaton.

- **[Thinking Like Transformers](https://arxiv.org/abs/2106.06981)**  
  Technion, Bar-Ilan University / AI2 · *ICML 2021* · 2021-06 · `📄 peer-reviewed` · 222 citations (S2)  
  [[Paper](https://arxiv.org/abs/2106.06981)]  
  Proposes RASP, a programming language whose primitives map transformer-encoder attention and feed-forward computation. Provides RASP programs for histograms, sorting and Dyck-languages, relates task difficulty to required layers and heads, and shows a transformer can be trained to mimic a RASP solution.

- **[What learning algorithm is in-context learning? Investigations with linear models](https://arxiv.org/abs/2211.15661)**  
  Ekin Akyürek et al. · *ICLR 2023* · 2022-11 · `📄 peer-reviewed` · 833 citations (S2)  
  [[Paper](https://arxiv.org/abs/2211.15661)]  
  Proves by construction that transformers can implement gradient descent and closed-form ridge regression for linear models. Shows trained in-context learners match gradient descent, ridge and least-squares predictors, with preliminary evidence of shared algorithmic features in late layers.

- **[Transformers Learn In-Context by Gradient Descent](https://arxiv.org/abs/2212.07677)**  
  ETH Zürich / Google Research · *ICML 2023* · 2022-12 · `📄 peer-reviewed` · 932 citations (S2)  
  [[Paper](https://arxiv.org/abs/2212.07677)]  
  Gives a simple weight construction showing a single linear self-attention layer matches gradient descent on a regression loss. Shows empirically that self-attention-only Transformers trained on regression tasks match gradient-descent models or the construction's weights.

- **[Looped Transformers as Programmable Computers](https://arxiv.org/abs/2301.13196)**  
  UW–Madison and others · *ICML 2023* · 2023-01 · `📄 peer-reviewed` · 319 citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.13196)]  
  Programs transformers with specific weights and places them in a loop, with the input sequence acting as a punchcard. Emulates a small instruction-set computer, mapping iterative algorithms to programs run by a looped, 13-layer transformer.

- **[Tracr: Compiled Transformers as a Laboratory for Interpretability](https://arxiv.org/abs/2301.05062)**  
  David Lindner et al. · *NeurIPS 2023* · 2023-01-12 · `📄 peer-reviewed` · 125 citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.05062)] [[Code](https://github.com/google-deepmind/tracr)] ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/tracr?style=social)  
  Compiles RASP programs into transformer weights with known structure.

- **[Learning Transformer Programs](https://arxiv.org/abs/2306.01128)**  
  Dan Friedman, Alexander Wettig, Danqi Chen · *NeurIPS 2023* · 2023-06 · `📄 peer-reviewed` · 60 citations (S2)  
  [[Paper](https://arxiv.org/abs/2306.01128)]  
  Trains modified Transformers that are then converted into discrete, human-readable programs, building on RASP. Learns programs for in-context learning, sorting, Dyck languages, named entity recognition and text classification, performing on par with standard Transformers of comparable size.

### Rule insertion and extraction

- **[Connectionist expert systems](https://doi.org/10.1145/42372.42377)**  
  Northeastern University · *Communications of the ACM* · 1988 · `📄 peer-reviewed` · 715 citations (S2)  
  [[Paper](https://doi.org/10.1145/42372.42377)]  
  Builds an expert system on a connectionist network (MACIE) and explains its conclusions by inspecting which weighted inputs determined each unit's output.

- **[Medical diagnostic expert system based on PDP model](https://doi.org/10.1109/ICNN.1988.23855)**  
  NTT · *Proc. IEEE ICNN'88* · 1988 · `📄 peer-reviewed` · 250 citations (S2)  
  [[Paper](https://doi.org/10.1109/ICNN.1988.23855)]  
  Extracts if-then rules from a backpropagation network trained for medical diagnosis, at NTT. Presents a diagnostic expert system built on a parallel distributed processing model, with rules read from the trained network.

- **[A distributed connectionist production system](https://doi.org/10.1207/s15516709cog1203_4)**  
  Carnegie Mellon University · *Cognitive Science* · 1988 · `📄 peer-reviewed` · 330 citations (S2)  
  [[Paper](https://doi.org/10.1207/s15516709cog1203_4)]  
  Implements rule matching and variable binding in a distributed connectionist production system, a network built to carry out symbolic rules.

- **[Interpreting neural-network connection weights](https://doi.org/10.5555/129449.129452)**  
  G.D. Garson · *AI Expert* · 1991 · `📄 peer-reviewed` · 1.5k citations (OA)  
  [[Paper](https://doi.org/10.5555/129449.129452)]  
  Proposes a weight-product measure of each input's importance, computed from the connection weights alone with no data.

- **[Rule induction through integrated symbolic and subsymbolic processing](https://proceedings.neurips.cc/paper_files/paper/1991/hash/cf67355a3333e6e143439161adc2d82e-Abstract.html)**  
  U. Colorado Boulder · *NIPS 1991* · 1992 · `📄 peer-reviewed` · 65 citations (S2)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1991/hash/cf67355a3333e6e143439161adc2d82e-Abstract.html)]  
  Describes RuleNet, which alternates learning with projecting the network's weights onto explicit rules and re-inserting those rules into the network.

- **[Extraction, insertion and refinement of symbolic rules in dynamically driven recurrent neural networks](https://doi.org/10.1080/09540099308915703)**  
  NEC Research Institute / RPI; OpenAlex lists U. Maryland and RPI · *Connection Science* · 1993 · `📄 peer-reviewed` · 110 citations (S2)  
  [[Paper](https://doi.org/10.1080/09540099308915703)]  
  Inserts known DFA transitions into second-order recurrent networks by programming a subset of weights to large values (±H), trains the network, then extracts refined automata by clustering hidden states, all in one paper.

- **[Extracting refined rules from knowledge-based neural networks](https://doi.org/10.1007/BF00993103)**  
  U. Wisconsin–Madison · *Machine Learning* · 1993 · `📄 peer-reviewed` · 760 citations (OA)  
  [[Paper](https://doi.org/10.1007/BF00993103)]  
  Extracts rules from trained knowledge-based networks by clustering weights and rewriting each unit as an 'M of these N antecedents' rule. Together with KBANN, it closes the knowledge-to-weights-to-knowledge loop.

- **[Knowledge-based artificial neural networks](https://doi.org/10.1016/0004-3702(94)90105-8)**  
  U. Wisconsin–Madison · *Artificial Intelligence* · 1994 · `📄 peer-reviewed` · 900 citations (S2)  
  [[Paper](https://doi.org/10.1016/0004-3702(94)90105-8)]  
  Turns each propositional Horn clause into a unit whose weights (±ω) and bias are set analytically, adds low-weight links, then refines the network by backpropagation: a compiler from knowledge to weights.

- **[Rule generation from neural networks](https://doi.org/10.1109/21.299696)**  
  University of Florida · *IEEE Trans. Systems, Man, and Cybernetics* · 1994 · `📄 peer-reviewed` · 410 citations (S2)  
  [[Paper](https://doi.org/10.1109/21.299696)]  
  Introduces the KT algorithm, which generates rules from a trained neural network by searching subsets of each unit's incoming weights.

- **[Survey and critique of techniques for extracting rules from trained artificial neural networks](https://doi.org/10.1016/0950-7051(96)81920-4)**  
  Queensland University of Technology · *Knowledge-Based Systems* · 1995 · `📄 peer-reviewed` · 1.4k citations (S2)  
  [[Paper](https://doi.org/10.1016/0950-7051(96)81920-4)]  
  Surveys techniques for extracting rules from trained networks and fixes the decompositional versus pedagogical taxonomy: read individual weights and units, or treat the network as a black box.

- **[Extracting tree-structured representations of trained networks](https://proceedings.neurips.cc/paper_files/paper/1995/hash/45f31d16b1058d586fc3be7207b58053-Abstract.html)**  
  U. Wisconsin–Madison · *NIPS 1995* · 1996 · `📄 peer-reviewed` · 434 citations (S2)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1995/hash/45f31d16b1058d586fc3be7207b58053-Abstract.html)]  
  Extracts tree-structured representations (TREPAN) from trained networks by querying the network as an oracle rather than reading its weights.

- **[The truth will come to light: directions and challenges in extracting the knowledge embedded within trained artificial neural networks](https://doi.org/10.1109/72.728352)**  
  QUT / ANU · *IEEE Trans. Neural Networks* · 1998 · `📄 peer-reviewed` · 470 citations (S2)  
  [[Paper](https://doi.org/10.1109/72.728352)]  
  Reviews directions and open challenges in extracting the knowledge embedded in trained neural networks, following the decompositional and pedagogical split.

### Weight surgery and pruning

- **[Skeletonization: A technique for trimming the fat from a network via relevance assessment](https://proceedings.neurips.cc/paper_files/paper/1988/hash/07e1cd7dca89a1678042477183b7ac3f-Abstract.html)**  
  U. Colorado Boulder · *NIPS 1988* · 1989 · `📄 peer-reviewed` · 540 citations (OA)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1988/hash/07e1cd7dca89a1678042477183b7ac3f-Abstract.html)]  
  Introduces skeletonization, which assesses the relevance of units in a trained network and deletes the least relevant ones. The aim is a minimal network that is more interpretable.

- **[Optimal brain damage](https://proceedings.neurips.cc/paper_files/paper/1989/hash/6c9882bbac1c7093bd25041881277658-Abstract.html)**  
  AT&T Bell Laboratories · *NIPS 1989* · 1990 · `📄 peer-reviewed` · 5.6k citations (S2)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1989/hash/6c9882bbac1c7093bd25041881277658-Abstract.html)]  
  Ranks weights by a saliency computed from a diagonal approximation of the Hessian and deletes the lowest-ranked ones. Bell Labs authors present it as a way to prune trained networks.

- **[A simple procedure for pruning back-propagation trained neural networks](https://doi.org/10.1109/72.80236)**  
  IBM Haifa Research · *IEEE Trans. Neural Networks* · 1990 · `📄 peer-reviewed` · 750 citations (S2)  
  [[Paper](https://doi.org/10.1109/72.80236)]  
  Proposes a simple procedure for pruning back-propagation trained networks by estimating the sensitivity of the error to each weight and removing low-sensitivity weights.

- **[Creating artificial neural networks that generalize](https://doi.org/10.1016/0893-6080(91)90033-2)**  
  Defence Science and Technology Organisation · *Neural Networks* · 1991 · `📄 peer-reviewed` · 690 citations (S2)  
  [[Paper](https://doi.org/10.1016/0893-6080(91)90033-2)]  
  Studies how to build networks that generalize, pruning hidden units whose outputs are constant or duplicate other units.

- **[Second order derivatives for network pruning: Optimal Brain Surgeon](https://proceedings.neurips.cc/paper_files/paper/1992/hash/303ed4c69846ab36c2904d3ba8573050-Abstract.html)**  
  Stanford University / Ricoh California Research Center · *NIPS 1992* · 1993 · `📄 peer-reviewed` · 2.2k citations (S2)  
  [[Paper](https://proceedings.neurips.cc/paper_files/paper/1992/hash/303ed4c69846ab36c2904d3ba8573050-Abstract.html)]  
  Uses the full inverse Hessian to choose which weight to delete and to compute a closed-form update for all remaining weights. The update is commonly written δw = −(w_q/[H⁻¹]_qq) H⁻¹ e_q.

- **[Pruning algorithms — a survey](https://doi.org/10.1109/72.248452)**  
  University of Washington · *IEEE Trans. Neural Networks* · 1993 · `📄 peer-reviewed` · 1.9k citations (S2)  
  [[Paper](https://doi.org/10.1109/72.248452)]  
  Surveys pruning algorithms for neural networks, from sensitivity-based weight removal to penalty terms, consolidating the field as of 1993.

- **[Net2Net: Accelerating Learning via Knowledge Transfer](https://arxiv.org/abs/1511.05641)**  
  Google · *ICLR 2016* · 2015-11 · `📄 peer-reviewed` · 825 citations (S2)  
  [[Paper](https://arxiv.org/abs/1511.05641)]  
  Transfers the information in a trained network into a wider or deeper network through function-preserving transformations, so the new network starts with the same function. Reports a new state-of-the-art ImageNet accuracy after adding depth to Inception modules.

- **[Network Morphism](https://arxiv.org/abs/1603.01670)**  
  Microsoft Research Asia + SUNY Buffalo · *ICML 2016* · 2016-03 · `📄 peer-reviewed` · 207 citations (S2)  
  [[Paper](https://arxiv.org/abs/1603.01670)]  
  Studies how to morph a trained network into a new one that completely preserves its function. Introduces network morphism equations and algorithms for changes of depth, width, kernel size and subnet, plus parametric activations for non-linearities.

- **[The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)**  
  Jonathan Frankle, Michael Carbin · *ICLR 2019* · 2018-03 · `📄 peer-reviewed` · 4.6k citations (S2)  
  [[Paper](https://arxiv.org/abs/1803.03635)]  
  Proposes that dense, randomly initialized networks contain subnetworks that reach comparable test accuracy when trained in isolation. Finds winning tickets under 10-20% of the size of fully-connected and convolutional networks on MNIST and CIFAR10.

- **[Are Sixteen Heads Really Better than One?](https://arxiv.org/abs/1905.10650)**  
  CMU + Facebook AI Research · *NeurIPS 2019* · 2019-05 · `📄 peer-reviewed` · 1.6k citations (S2)  
  [[Paper](https://arxiv.org/abs/1905.10650)]  
  Observes that a large percentage of attention heads can be removed at test time without significantly impacting performance, and some layers can be reduced to a single head. Also examines greedy pruning algorithms.

- **[Optimal Brain Compression: A Framework for Accurate Post-Training Quantization and Pruning](https://arxiv.org/abs/2208.11580)**  
  IST Austria · *NeurIPS 2022* · 2022-08 · `📄 peer-reviewed` · 461 citations (S2)  
  [[Paper](https://arxiv.org/abs/2208.11580)]  
  Introduces a framework covering weight pruning and quantization in the one-shot, post-training setting. It is built on an exact and efficient realization of the Optimal Brain Surgeon framework, extended to quantization.

- **[SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774)**  
  IST Austria · *ICML 2023* · 2023-01 · `📄 peer-reviewed` · 1.7k citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.00774)]  
  Prunes GPT-family models in one shot without retraining. Runs on OPT-175B and BLOOM-176B in under 4.5 hours, reaching 60% unstructured sparsity with negligible perplexity increase, ignoring more than 100 billion weights.

- **[A Simple and Effective Pruning Approach for Large Language Models (Wanda)](https://arxiv.org/abs/2306.11695)**  
  CMU, Meta AI, Bosch Center for AI · *ICLR 2024* · 2023-06 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2306.11695)]  
  Prunes pretrained LLMs by weight magnitude multiplied by input activation on a per-output basis. Requires no retraining or weight update, and is evaluated on LLaMA and LLaMA-2 against magnitude pruning.

### Fast weights and self-modifying networks

- **[The correlation theory of brain function](https://doi.org/10.1007/978-1-4612-4320-5_2)**  
  C. von der Malsburg · *Internal report, MPI Göttingen (reprinted 1994)* · 1981 · `📄 peer-reviewed` · 1.4k citations (S2)  
  [[Paper](https://doi.org/10.1007/978-1-4612-4320-5_2)]  
  Introduces dynamic links: synapses that change on a fast timescale to bind features temporarily, the earliest form of fast weights.

- **[Learning to control fast-weight memories: An alternative to dynamic recurrent networks](https://doi.org/10.1162/neco.1992.4.1.131)**  
  J. Schmidhuber · *Neural Computation* · 1992 · `📄 peer-reviewed` · 640 citations (S2)  
  [[Paper](https://doi.org/10.1162/neco.1992.4.1.131)]  
  Describes a slow network that learns to output context-dependent weight changes for a second, fast network, so one net programs another net's weights on the fly. Offered as an alternative to dynamic recurrent networks.

- **[A 'self-referential' weight matrix](https://doi.org/10.1007/978-1-4471-2063-6_107)**  
  J. Schmidhuber · *Proc. ICANN '93, Springer* · 1993 · `📄 peer-reviewed` · 117 citations (S2)  
  [[Paper](https://doi.org/10.1007/978-1-4471-2063-6_107)]  
  Adds special units that let a network address, read and modify any of its own weights, including the weights of the modification machinery itself, defining a self-referential weight matrix.

- **[Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](https://arxiv.org/abs/cs/0309048)**  
  Jürgen Schmidhuber · *Preprint* · 2003-09 · `📝 preprint` · 120 citations (S2)  
  [[Paper](https://arxiv.org/abs/cs/0309048)]  
  Presents self-referential problem solvers that rewrite any part of their own code once a proof searcher finds a proof the rewrite is useful. Shows such a self-rewrite is globally optimal, with no local maxima.

- **[Using Fast Weights to Attend to the Recent Past](https://arxiv.org/abs/1610.06258)**  
  Jimmy Ba et al. · *NeurIPS 2016* · 2016-10 · `📄 peer-reviewed` · 386 citations (S2)  
  [[Paper](https://arxiv.org/abs/1610.06258)]  
  Adds fast weights, variables that change slower than activities but faster than standard weights, as temporary memory of the recent past. Provides a neurally plausible form of attention to the past without storing copies of neural activity patterns.

- **[Neural Network Quine](https://arxiv.org/abs/1803.05859)**  
  Oscar Chang, Hod Lipson · *IEEE ALIFE 2018* · 2018-03 · `📄 peer-reviewed` · 28 citations (S2)  
  [[Paper](https://arxiv.org/abs/1803.05859)]  
  Builds self-replicating neural networks that replicate by learning to output their own weights, trained with a loss function and a regeneration method. Also adds an MNIST classification task, observing a trade-off between classification and replication.

- **[Linear Transformers Are Secretly Fast Weight Programmers](https://arxiv.org/abs/2102.11174)**  
  Imanol Schlag, Kazuki Irie, Jürgen Schmidhuber · *ICML 2021* · 2021-02 · `📄 peer-reviewed` · 651 citations (S2)  
  [[Paper](https://arxiv.org/abs/2102.11174)]  
  Shows the formal equivalence of linearised self-attention and early-1990s fast weight controllers, where a slow net programs another net's fast weights through additive outer products. Replaces additive updates with a delta-rule-like instruction and tests on retrieval, translation and language modelling.

- **[A Modern Self-Referential Weight Matrix That Learns to Modify Itself](https://arxiv.org/abs/2202.05780)**  
  Kazuki Irie, Imanol Schlag, Róbert Csordás, Jürgen Schmidhuber · *ICML 2022* · 2022-02 · `📄 peer-reviewed` · 52 citations (S2)  
  [[Paper](https://arxiv.org/abs/2202.05780)]  
  Proposes a scalable self-referential weight matrix that uses outer products and the delta update rule to modify itself during runtime. Evaluates it on supervised few-shot learning and multi-task reinforcement learning with procedurally generated game environments.

- **[Eliminating Meta Optimization Through Self-Referential Meta Learning](https://arxiv.org/abs/2212.14392)**  
  Louis Kirsch, Jürgen Schmidhuber · *Preprint* · 2022-12 · `📝 preprint` · 14 citations (S2)  
  [[Paper](https://arxiv.org/abs/2212.14392)]  
  Investigates self-referential meta learning systems that modify themselves without explicit meta optimization. Proposes fitness monotonic execution, in which a network self-modifies on bandit and classic control tasks by receiving more computational resources when it performs better.

- **[Learning to (Learn at Test Time): RNNs with Expressive Hidden States](https://arxiv.org/abs/2407.04620)**  
  Yu Sun et al. · *ICML 2025* · 2024-07 · `📄 peer-reviewed` · 441 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.04620)]  
  Makes the hidden state of a sequence layer a machine learning model, updated by a step of self-supervised learning even on test sequences. Evaluates TTT-Linear and TTT-MLP at 125M to 1.3B parameters against Transformer and Mamba.

- **[Titans: Learning to Memorize at Test Time](https://arxiv.org/abs/2501.00663)**  
  Ali Behrouz, Peilin Zhong, Vahab Mirrokni · *Preprint* · 2024-12 · `📝 preprint` · 422 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.00663)]  
  Introduces a neural long-term memory module that learns to memorize historical context at test time, combined with attention in a family of three architecture variants. Reports scaling to context windows larger than 2M.

### Neuroevolution and gradient-free weight search

- **[Training feedforward neural networks using genetic algorithms](https://ijcai.org/proceedings/1989/122)**  
  D.J. Montana, L. Davis · *Proc. 11th IJCAI* · 1989 · `📄 peer-reviewed`  
  [[Paper](https://ijcai.org/proceedings/1989/122)]  
  Applies a genetic algorithm directly to weight space, evolving real-valued weight genomes for a feedforward sonar classifier. It is one of the first uses of genetic algorithms to set network weights in 1989.

- **[Genetic algorithms and neural networks: optimizing connections and connectivity](https://doi.org/10.1016/0167-8191(90)90086-O)**  
  D. Whitley, T. Starkweather, C. Bogart · *Parallel Computing* · 1990 · `📄 peer-reviewed` · 810 citations (S2)  
  [[Paper](https://doi.org/10.1016/0167-8191(90)90086-O)]  
  Uses the GENITOR genetic algorithm to optimize a network's weights and its connectivity together, treating both as a single search problem rather than training weights by gradient descent on a fixed topology.

- **[Designing neural networks using genetic algorithms with graph generation system](https://www.complex-systems.com/abstracts/v04_i04_a06/)**  
  Center for Machine Translation, CMU, and NEC Corporation, Tokyo · *Complex Systems* · 1990 · `📄 peer-reviewed`  
  [[Paper](https://www.complex-systems.com/abstracts/v04_i04_a06/)]  
  Evolves graph-grammar rules with a genetic algorithm, and the rules emit the network's connectivity matrix. The search runs over programs that generate networks instead of over the networks themselves.

- **[Automatic definition of modular neural networks](https://doi.org/10.1177/105971239400300202)**  
  ENS Lyon · *Adaptive Behavior* · 1994 · `📄 peer-reviewed` · 320 citations (S2)  
  [[Paper](https://doi.org/10.1177/105971239400300202)]  
  Presents cellular encoding, which a thesis record calls a machine language for neural networks. It comes with a compiler from a high-level language, so evolution and explicit compilation share one representation.

- **[Evolving artificial neural networks](https://doi.org/10.1109/5.784219)**  
  X. Yao · *Proceedings of the IEEE* · 1999 · `📄 peer-reviewed` · 2.2k citations (S2)  
  [[Paper](https://doi.org/10.1109/5.784219)]  
  Reviews the field of evolving neural networks and gives a taxonomy that separates direct encodings from indirect encodings. It is published in Proceedings of the IEEE in 1999.

- **[Evolving neural networks through augmenting topologies](https://doi.org/10.1162/106365602320169811)**  
  University of Texas at Austin · *Evolutionary Computation* · 2002 · `📄 peer-reviewed` · 3.8k citations (S2)  
  [[Paper](https://doi.org/10.1162/106365602320169811)]  
  Introduces NEAT, a method that evolves connection weights and network topology together. It links the early neuroevolution work to the modern era.

- **[Compositional pattern producing networks: A novel abstraction of development](https://doi.org/10.1007/s10710-007-9028-8)**  
  UCF · *Genetic Programming and Evolvable Machines* · 2007 · `📄 peer-reviewed` · 853 citations (S2)  
  [[Paper](https://doi.org/10.1007/s10710-007-9028-8)]  
  Introduces compositional pattern producing networks, small evolved networks that generate patterns; HyperNEAT later uses them to paint the weights of large, geometrically regular networks.

- **[A Hypercube-Based Encoding for Evolving Large-Scale Neural Networks](https://doi.org/10.1162/artl.2009.15.2.15202)**  
  Univ. of Central Florida · *Artificial Life* · 2009 · `📄 peer-reviewed` · 894 citations (S2)  
  [[Paper](https://doi.org/10.1162/artl.2009.15.2.15202)]  
  Introduces HyperNEAT, a hypercube-based indirect encoding in which a small evolved network generates the weights of a large, geometrically regular network, used to evolve large-scale neural networks.

- **[Evolving large-scale neural networks for vision-based reinforcement learning](https://doi.org/10.1145/2463372.2463509)**  
  IDSIA · *GECCO 2013* · 2013 · `📄 peer-reviewed` · 173 citations (S2)  
  [[Paper](https://doi.org/10.1145/2463372.2463509)]  
  Encodes a network of over 1M weights as a few DCT coefficients and evolves those coefficients. The resulting network learns to drive in the TORCS simulator directly from pixels.

- **[Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://arxiv.org/abs/1703.03864)**  
  OpenAI · *Preprint* · 2017-03 · `📝 preprint` · 1.9k citations (S2)  
  [[Paper](https://arxiv.org/abs/1703.03864)]  
  Tests Evolution Strategies, a black-box optimizer, as an alternative to MDP-based RL on MuJoCo and Atari. Communicating only scalars lets it scale to over a thousand workers, solving 3D humanoid walking in 10 minutes.

- **[Deep Neuroevolution: Genetic Algorithms Are a Competitive Alternative for Training Deep Neural Networks for Reinforcement Learning](https://arxiv.org/abs/1712.06567)**  
  Uber AI Labs · *Preprint* · 2017-12 · `📝 preprint` · 785 citations (S2)  
  [[Paper](https://arxiv.org/abs/1712.06567)]  
  Evolves DNN weights with a simple gradient-free genetic algorithm that performs well on Atari and humanoid locomotion. It evolves networks with over four million free parameters, the largest evolved with a traditional evolutionary algorithm.

- **[Evolution Strategies at Scale: LLM Fine-Tuning Beyond Reinforcement Learning](https://arxiv.org/abs/2509.24372)**  
  Xin Qiu et al. · *Preprint* · 2025-09 · `📝 preprint` · 44 citations (S2)  
  [[Paper](https://arxiv.org/abs/2509.24372)]  
  Applies evolution strategies to full-parameter fine-tuning of LLMs at the billion-parameter scale, without dimensionality reduction. The paper reports that it outperforms established RL implementations on several axes, including tolerance to delayed rewards and stability.

### Hypernetworks and weight generation

- **[Predicting Parameters in Deep Learning](https://arxiv.org/abs/1306.0543)**  
  Misha Denil et al. · *NeurIPS 2013* · 2013-06 · `📄 peer-reviewed` · 1.5k citations (S2)  
  [[Paper](https://arxiv.org/abs/1306.0543)]  
  Shows that a small set of weight values per feature can predict the remaining weights of several deep learning architectures. In the best case, more than 95% of a network's weights are predicted without any drop in accuracy.

- **[Dynamic Filter Networks](https://arxiv.org/abs/1605.09673)**  
  Bert De Brabandere, Xu Jia, Tinne Tuytelaars, Luc Van Gool · *NeurIPS 2016* · 2016-05 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/1605.09673)]  
  Introduces a layer whose convolution filters are generated dynamically from the input rather than fixed after training. Reaches state-of-the-art on moving MNIST with a much smaller model, and demonstrates video and stereo prediction.

- **[Learning to learn by gradient descent by gradient descent](https://arxiv.org/abs/1606.04474)**  
  Marcin Andrychowicz et al. · *NeurIPS 2016* · 2016-06 · `📄 peer-reviewed` · 2.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/1606.04474)]  
  Casts the design of an optimization algorithm as a learning problem, implementing learned optimizers with LSTMs. They outperform hand-designed competitors on trained tasks and generalize to new tasks with similar structure, including neural network training and neural art.

- **[HyperNetworks](https://arxiv.org/abs/1609.09106)**  
  David Ha, Andrew M. Dai, Quoc V. Le · *ICLR 2017* · 2016-09 · `📄 peer-reviewed` · 2.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/1609.09106)]  
  Introduces hypernetworks, where one network generates the weights of another, trained end-to-end with backpropagation. Generates non-shared LSTM weights with near state-of-the-art sequence modelling results, and gives respectable image recognition results with fewer learnable parameters.

- **[SMASH: One-Shot Model Architecture Search through HyperNetworks](https://arxiv.org/abs/1708.05344)**  
  Andrew Brock, Theodore Lim, J. M. Ritchie, Nick Weston · *ICLR 2018* · 2017-08 · `📄 peer-reviewed` · 855 citations (S2)  
  [[Paper](https://arxiv.org/abs/1708.05344)]  
  Trains an auxiliary HyperNet that generates the weights of a main model conditioned on its architecture. Validation performance of networks with generated weights ranks architectures at the cost of one training run, tested on CIFAR-10, CIFAR-100, STL-10, ModelNet10 and Imagenet32x32.

- **[Meta-Learning with Latent Embedding Optimization](https://arxiv.org/abs/1807.05960)**  
  Andrei A. Rusu et al. · *ICLR 2019* · 2018-07 · `📄 peer-reviewed` · 1.6k citations (S2)  
  [[Paper](https://arxiv.org/abs/1807.05960)]  
  Learns a data-dependent latent generative representation of model parameters and performs gradient-based meta-learning in that low-dimensional latent space. Reports state-of-the-art few-shot classification on miniImageNet and tieredImageNet.

- **[Graph HyperNetworks for Neural Architecture Search](https://arxiv.org/abs/1810.05749)**  
  Chris Zhang, Mengye Ren, Raquel Urtasun · *ICLR 2019* · 2018-10 · `📄 peer-reviewed` · 307 citations (S2)  
  [[Paper](https://arxiv.org/abs/1810.05749)]  
  Proposes a graph neural network hypernetwork that generates weights for a given architecture by inference over its topology. Random architectures scored with generated weights let search run nearly 10 times faster than other random search methods on CIFAR-10 and ImageNet.

- **[Parameter Prediction for Unseen Deep Architectures](https://arxiv.org/abs/2110.13100)**  
  Boris Knyazev, Michal Drozdzal, Graham W. Taylor, Adriana Romero-Soriano · *NeurIPS 2021* · 2021-10 · `📄 peer-reviewed` · 114 citations (S2)  
  [[Paper](https://arxiv.org/abs/2110.13100)]  
  Introduces the DeepNets-1M dataset of architecture graphs and a graph hypernetwork that predicts parameters in one forward pass. It predicts all 24 million parameters of a ResNet-50, reaching 60% accuracy on CIFAR-10.

- **[HyperTransformer: Model Generation for Supervised and Semi-Supervised Few-Shot Learning](https://arxiv.org/abs/2201.04182)**  
  Andrey Zhmoginov, Mark Sandler, Max Vladymyrov · *ICML 2022* · 2022-01 · `📄 peer-reviewed` · 87 citations (S2)  
  [[Paper](https://arxiv.org/abs/2201.04182)]  
  Uses a Transformer to generate the weights of a convolutional network directly from support samples for few-shot learning. For larger target models, generating only the last layer gives results competitive with or better than state-of-the-art methods.

- **[Learning to Learn with Generative Models of Neural Network Checkpoints](https://arxiv.org/abs/2209.12892)**  
  William Peebles et al. · *Preprint* · 2022-09 · `📝 preprint` · 109 citations (S2)  
  [[Paper](https://arxiv.org/abs/2209.12892)]  
  Trains a conditional diffusion transformer on a dataset of network checkpoints. Given initial parameters and a prompted loss, error or return, it predicts parameter updates achieving that metric, optimizing unseen parameters in one update.

- **[VeLO: Training Versatile Learned Optimizers by Scaling Up](https://arxiv.org/abs/2211.09760)**  
  Luke Metz et al. · *Preprint* · 2022-11 · `📝 preprint` · 90 citations (S2)  
  [[Paper](https://arxiv.org/abs/2211.09760)]  
  Trains a small neural network optimizer that ingests gradients and outputs parameter updates, meta-trained with approximately four thousand TPU-months of compute. It needs no hyperparameter tuning; code, data and a benchmark suite are open-sourced.

- **[Neural Network Diffusion](https://arxiv.org/abs/2402.13144)**  
  Kai Wang et al. · *Preprint* · 2024-02 · `📝 preprint` · 65 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.13144)]  
  Trains an autoencoder on a subset of trained network parameters, then a diffusion model on its latents, to synthesize new parameters. Generated models match or improve on trained networks across architectures and datasets, without memorizing them.

### Model editing

- **[GAN Dissection: Visualizing and Understanding Generative Adversarial Networks](https://arxiv.org/abs/1811.10597)**  
  David Bau et al. · *ICLR 2019* · 2018-11 · `📄 peer-reviewed` · 525 citations (S2)  
  [[Paper](https://arxiv.org/abs/1811.10597)]  
  Presents a framework to visualize GANs at unit, object and scene level, identifying interpretable units tied to object concepts and measuring their causal effect through interventions. Locating and removing artifact-causing units improves GAN outputs.

- **[Editable Neural Networks](https://arxiv.org/abs/2004.00345)**  
  Yandex + HSE University · *ICLR 2020* · 2020-04 · `📄 peer-reviewed` · 232 citations (S2)  
  [[Paper](https://arxiv.org/abs/2004.00345)]  
  Introduces Editable Training, a model-agnostic training technique that encourages fast editing of a trained model, patching a mistake on one sample without changing behavior on other samples. Tests it on large-scale image classification and machine translation.

- **[Rewriting a Deep Generative Model](https://arxiv.org/abs/2007.15646)**  
  MIT CSAIL + Adobe Research · *ECCV 2020* · 2020-07 · `📄 peer-reviewed` · 165 citations (S2)  
  [[Paper](https://arxiv.org/abs/2007.15646)]  
  Treats a layer of a deep generative model as a linear associative memory and derives an algorithm to modify one entry, changing a rule. Includes an interactive interface and outperforms fine-tuning and edit-transfer baselines on multiple datasets.

- **[Editing Factual Knowledge in Language Models](https://arxiv.org/abs/2104.08164)**  
  University of Amsterdam · *EMNLP 2021* · 2021-04 · `📄 peer-reviewed` · 781 citations (S2)  
  [[Paper](https://arxiv.org/abs/2104.08164)]  
  Trains a hyper-network with constrained optimization to predict the weight update that changes one fact without affecting other knowledge. Tests it on a BERT fact-checking model and a BART question-answering model, with paraphrases changing consistently.

- **[Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696)**  
  Peking University + Microsoft Research · *ACL 2022* · 2021-04 · `📄 peer-reviewed` · 804 citations (S2)  
  [[Paper](https://arxiv.org/abs/2104.08696)]  
  Introduces a knowledge attribution method that identifies neurons expressing a relational fact in BERT on cloze tasks. Finds their activation correlates positively with the fact's expression, and case studies update and erase facts without fine-tuning.

- **[Fast Model Editing at Scale](https://arxiv.org/abs/2110.11309)**  
  Stanford · *ICLR 2022* · 2021-10 · `📄 peer-reviewed` · 645 citations (S2)  
  [[Paper](https://arxiv.org/abs/2110.11309)]  
  Introduces MEND, small auxiliary editing networks that transform the fine-tuning gradient with a low-rank decomposition to make fast, local edits from one input-output pair. Trains on a single GPU in under a day for models of 10 billion+ parameters.

- **[Editing a classifier by rewriting its prediction rules](https://arxiv.org/abs/2112.01008)**  
  MIT · *NeurIPS 2021* · 2021-12 · `📄 peer-reviewed` · 105 citations (S2)  
  [[Paper](https://arxiv.org/abs/2112.01008)]  
  Presents a methodology for modifying a classifier's behavior by directly rewriting its prediction rules. Requires virtually no additional data collection and applies to adapting a model to new environments and ignoring spurious features.

- **[Locating and Editing Factual Associations in GPT (ROME)](https://arxiv.org/abs/2202.05262)**  
  Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov · *NeurIPS 2022* · 2022-02-10 · `📄 peer-reviewed` · 3.7k citations (S2)  
  [[Paper](https://arxiv.org/abs/2202.05262)] [[Code](https://github.com/kmeng01/rome)] [[Project](https://rome.baulab.info/)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/rome?style=social)  
  Rank-one edits to a single MLP layer rewrite a stored fact.

- **[Memory-Based Model Editing at Scale](https://arxiv.org/abs/2206.06520)**  
  Stanford · *ICML 2022* · 2022-06 · `📄 peer-reviewed` · 627 citations (S2)  
  [[Paper](https://arxiv.org/abs/2206.06520)]  
  Introduces SERAC, which stores edits in an explicit memory and learns to reason over them to modulate the base model's predictions. Adds three editing problems on question answering, fact-checking and dialogue; only SERAC performs well on all three.

- **[Mass-Editing Memory in a Transformer (MEMIT)](https://arxiv.org/abs/2210.07229)**  
  Kevin Meng, Arnab Sen Sharma, Alex Andonian, Yonatan Belinkov, David Bau · *ICLR 2023* · 2022-10-13 · `📄 peer-reviewed` · 1.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/2210.07229)] [[Code](https://github.com/kmeng01/memit)] [[Project](https://memit.baulab.info/)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/memit?style=social)  
  Extends ROME to thousands of edits at once across several layers.

- **[Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models](https://arxiv.org/abs/2301.04213)**  
  Google Research + UNC Chapel Hill · *NeurIPS 2023* · 2023-01 · `📄 peer-reviewed` · 321 citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.04213)]  
  Shows that causal-tracing localization conclusions do not indicate which MLP layer is best to edit to override a stored fact. Also studies erasing and amplifying facts, where the edited layer predicts performance better than localization does.

- **[Unified Concept Editing in Diffusion Models](https://arxiv.org/abs/2308.14761)**  
  Northeastern/MIT/Technion · *WACV 2024* · 2023-08 · `📄 peer-reviewed` · 499 citations (S2)  
  [[Paper](https://arxiv.org/abs/2308.14761)]  
  Presents UCE, which edits text-to-image diffusion models without training, using a closed-form solution on text-conditional projections. Demonstrates simultaneous debiasing, style erasure and content moderation, with improved efficacy and scalability over prior work.

- **[AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://arxiv.org/abs/2410.02355)**  
  USTC + National University of Singapore · *ICLR 2025* · 2024-10 · `📄 peer-reviewed` · 324 citations (S2)  
  [[Paper](https://arxiv.org/abs/2410.02355)]  
  Projects the perturbation of locate-then-edit methods onto the null space of preserved knowledge before applying it to parameters. Boosts most such methods by an average of 36.7% on LLaMA3, GPT2-XL and GPT-J with one added line of code.

### Weight arithmetic and merging

- **[Loss Surfaces, Mode Connectivity, and Fast Ensembling of DNNs](https://arxiv.org/abs/1802.10026)**  
  Garipov et al. · *NeurIPS 2018* · 2018-02 · `📄 peer-reviewed` · 1k citations (S2)  
  [[Paper](https://arxiv.org/abs/1802.10026)]  
  Shows that optima of deep network loss functions are connected by simple curves along which training and test accuracy stay nearly constant. Introduces a procedure to find them, and Fast Geometric Ensembling, which trains ensembles in the time of one model.

- **[Averaging Weights Leads to Wider Optima and Better Generalization](https://arxiv.org/abs/1803.05407)**  
  Izmailov et al. · *UAI 2018* · 2018-03 · `📄 peer-reviewed` · 2.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/1803.05407)]  
  Averages multiple points along the SGD trajectory with a cyclical or constant learning rate. Finds flatter solutions than SGD and approximates Fast Geometric Ensembling with one model. Improves test accuracy on CIFAR-10, CIFAR-100 and ImageNet across several architectures.

- **[Linear Mode Connectivity and the Lottery Ticket Hypothesis](https://arxiv.org/abs/1912.05671)**  
  Frankle, Dziugaite, Roy, Carbin · *ICML 2020* · 2019-12 · `📄 peer-reviewed` · 881 citations (S2)  
  [[Paper](https://arxiv.org/abs/1912.05671)]  
  Studies whether networks reach the same linearly connected minimum under different SGD noise. Finds vision models become stable early in training, and shows lottery-ticket subnetworks reach full accuracy only when stable: at initialization on MNIST, early in training on ImageNet.

- **[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)**  
  Edward J. Hu et al. · *ICLR 2022* · 2021-06 · `📄 peer-reviewed` · 25.5k citations (S2)  
  [[Paper](https://arxiv.org/abs/2106.09685)]  
  Freezes pre-trained weights and injects trainable rank decomposition matrices into each Transformer layer. Compared with GPT-3 175B fine-tuned with Adam, it cuts trainable parameters 10,000 times and GPU memory 3 times, with on-par or better quality.

- **[Robust fine-tuning of zero-shot models](https://arxiv.org/abs/2109.01903)**  
  Wortsman et al. · *CVPR 2022* · 2021-09 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2109.01903)]  
  Introduces WiSE-FT, which ensembles the weights of zero-shot and fine-tuned models such as CLIP. On ImageNet and five derived distribution shifts it improves shifted accuracy by 4 to 6 pp over prior work and ImageNet accuracy by 1.6 pp.

- **[Merging Models with Fisher-Weighted Averaging](https://arxiv.org/abs/2111.09832)**  
  Matena, Raffel · *NeurIPS 2022* · 2021-11 · `📄 peer-reviewed` · 784 citations (S2)  
  [[Paper](https://arxiv.org/abs/2111.09832)]  
  Frames merging as choosing parameters that maximize joint posterior likelihood, approximating each posterior as a Gaussian with Fisher information as precision. Improves on simple averaging and is competitive with gradient-based transfer learning at lower cost.

- **[Model soups: averaging weights of multiple fine-tuned models improves accuracy without increasing inference time](https://arxiv.org/abs/2203.05482)**  
  Wortsman et al. · *ICML 2022* · 2022-03 · `📄 peer-reviewed` · 1.9k citations (S2)  
  [[Paper](https://arxiv.org/abs/2203.05482)]  
  Averages the weights of multiple models fine-tuned with different hyperparameters, adding no inference or memory cost. The resulting ViT-G model attains 90.94% top-1 accuracy on ImageNet, reported as a new state of the art.

- **[Git Re-Basin: Merging Models modulo Permutation Symmetries](https://arxiv.org/abs/2209.04836)**  
  Ainsworth, Hayase, Srinivasa · *ICLR 2023* · 2022-09 · `📄 peer-reviewed` · 606 citations (S2)  
  [[Paper](https://arxiv.org/abs/2209.04836)]  
  Introduces three algorithms that permute the hidden units of one model to align it with a reference model before merging in weight space. Demonstrates zero-barrier linear mode connectivity between independently trained ResNet models on CIFAR-10.

- **[Editing Models with Task Arithmetic](https://arxiv.org/abs/2212.04089)**  
  Gabriel Ilharco et al. · *ICLR 2023* · 2022-12-08 · `📄 peer-reviewed` · 1.4k citations (S2)  
  [[Paper](https://arxiv.org/abs/2212.04089)] [[Code](https://github.com/mlfoundations/task_vectors)] ![GitHub stars](https://img.shields.io/github/stars/mlfoundations/task_vectors?style=social)  
  Adding and subtracting fine-tuning weight differences (task vectors) steers a model's behavior.

- **[TIES-Merging: Resolving Interference When Merging Models](https://arxiv.org/abs/2306.01708)**  
  Yadav et al. · *NeurIPS 2023* · 2023-06 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2306.01708)]  
  Introduces TIES-Merging, which resets parameters that changed little during fine-tuning, resolves sign conflicts, and merges only parameters agreeing with the chosen sign. Reports outperforming existing merging methods across modalities, domains, task counts, model sizes and architectures.

- **[Language Models are Super Mario: Absorbing Abilities from Homologous Models as a Free Lunch](https://arxiv.org/abs/2311.03099)**  
  Yu et al. · *ICML 2024* · 2023-11 · `📄 peer-reviewed` · 911 citations (S2)  
  [[Paper](https://arxiv.org/abs/2311.03099)]  
  Introduces DARE, which randomly drops delta parameters with ratio p and rescales the rest by 1/(1−p). Eliminates 90% or even 99% of SFT deltas, merges task-specific models, and yields a 7B model ranking first on the Open LLM Leaderboard.

- **[Evolutionary optimization of model merging recipes](https://arxiv.org/abs/2403.13187)**  
  Akiba et al. · *Nature Machine Intelligence* · 2024-03 · `📄 peer-reviewed` · 283 citations (S2)  
  [[Paper](https://arxiv.org/abs/2403.13187)]  
  Proposes an evolutionary search that automatically finds combinations of open-source models, in both parameter space and data flow space. Produces a Japanese Math LLM and a Japanese VLM, reporting state-of-the-art results on Japanese benchmarks.

- **[Arcee's MergeKit: A Toolkit for Merging Large Language Models](https://arxiv.org/abs/2403.13257)**  
  Goddard et al. · *EMNLP 2024* · 2024-03 · `📄 peer-reviewed` · 263 citations (S2)  
  [[Paper](https://arxiv.org/abs/2403.13257)]  
  Introduces MergeKit, an open-source extensible library for merging language model parameters on any hardware. Reports that thousands of models have been merged by the community, including checkpoints assessed on the Open LLM Leaderboard.

### Weight-space learning

- **[Implicit Self-Regularization in Deep Neural Networks: Evidence from Random Matrix Theory and Implications for Learning](https://arxiv.org/abs/1810.01075)**  
  C. H. Martin, M. W. Mahoney · *JMLR* · 2018-10 · `📄 peer-reviewed` · 360 citations (S2)  
  [[Paper](https://arxiv.org/abs/1810.01075)]  
  Applies random matrix theory to layer weight matrices of pretrained and from-scratch networks, including AlexNet, Inception and LeNet5. Identifies 5+1 phases of training and a Heavy-Tailed Self-Regularization form in state-of-the-art models.

- **[Predicting Neural Network Accuracy from Weights](https://arxiv.org/abs/2002.11448)**  
  Unterthiner et al. · *Preprint* · 2020-02 · `📝 preprint` · 156 citations (S2)  
  [[Paper](https://arxiv.org/abs/2002.11448)]  
  Predicts a trained network's accuracy from simple weight statistics alone, ranking networks with R2 above 0.98. Releases 120k convolutional networks trained on four datasets; predictors transfer to unobserved datasets and architectures.

- **[Classifying the classifier: dissecting the weight space of neural networks](https://arxiv.org/abs/2002.05688)**  
  Eilertsen et al. · *ECAI 2020* · 2020-02 · `📄 peer-reviewed` · 81 citations (S2)  
  [[Paper](https://arxiv.org/abs/2002.05688)]  
  Trains meta-classifiers on weights to identify training-setup properties such as dataset, optimizer and architecture, using small subsets of consecutive weights. Releases the NWS dataset of 320K weight snapshots from 16K trained networks.

- **[Predicting trends in the quality of state-of-the-art neural networks without access to training or testing data](https://arxiv.org/abs/2002.06716)**  
  C. H. Martin, T. S. Peng, M. W. Mahoney · *Nature Communications 2021* · 2020-02 · `📄 peer-reviewed` · 188 citations (S2)  
  [[Paper](https://arxiv.org/abs/2002.06716)]  
  Meta-analyzes hundreds of public pretrained models without training or test data. Finds norm-based metrics correlate with test accuracy, while power-law metrics from heavy-tailed self-regularization theory better separate well-trained from poorly-trained models.

- **[Hyper-Representations: Self-Supervised Representation Learning on Neural Network Weights for Model Characteristic Prediction](https://arxiv.org/abs/2110.15288)**  
  Schürholt, Kostadinov, Borth · *NeurIPS 2021* · 2021-10 · `📄 peer-reviewed` · 17 citations (S2)  
  [[Paper](https://arxiv.org/abs/2110.15288)]  
  Learns representations of weights from populations of networks by self-supervised learning, with domain-specific augmentations and an adapted attention architecture. Recovers model characteristics and outperforms prior work predicting hyper-parameters, test accuracy and generalization gap.

- **[From data to functa: Your data point is a function and you can treat it like one](https://arxiv.org/abs/2201.12204)**  
  Dupont et al. · *ICML 2022* · 2022-01 · `📄 peer-reviewed` · 249 citations (S2)  
  [[Paper](https://arxiv.org/abs/2201.12204)]  
  Treats data points as implicit neural representations called functa and proposes a framework for deep learning on them. Applies it to images, 3D shapes, NeRFs and manifold data for generation, imputation, view synthesis and classification.

- **[Model Zoos: A Dataset of Diverse Populations of Neural Network Models](https://arxiv.org/abs/2209.14764)**  
  Schürholt et al. · *NeurIPS 2022 Datasets & Benchmarks* · 2022-09 · `📄 peer-reviewed` · 53 citations (S2)  
  [[Paper](https://arxiv.org/abs/2209.14764)]  
  Publishes 27 model zoos on eight image datasets, with 50,360 unique models plus sparsified twins, totaling over 3,844,360 model states. Provides analysis and benchmarks for studying weight-space structure across model populations.

- **[Detecting Backdoors with Meta-Models](https://mlanthology.org/neuripsw/2023/langosco2023neuripsw-detecting/)**  
  Langosco et al. · *NeurIPS 2023 Workshop* · 2023 · `📄 peer-reviewed`  
  [[Paper](https://mlanthology.org/neuripsw/2023/langosco2023neuripsw-detecting/)]  
  Trains meta-models on about 4,000 clean and backdoored CNNs to detect backdoors from weights. Detects i.i.d.-trigger backdoors with over 99% accuracy.

- **[Equivariant Architectures for Learning in Deep Weight Spaces](https://arxiv.org/abs/2301.12780)**  
  Navon et al. · *ICML 2023* · 2023-01 · `📄 peer-reviewed` · 133 citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.12780)]  
  Presents an architecture that takes an MLP's weights and biases as input, using layers equivariant to neuron-permutation symmetry. Characterizes all affine equivariant and invariant layers, built from pooling, broadcasting and fully connected operations.

- **[Permutation Equivariant Neural Functionals](https://arxiv.org/abs/2302.14040)**  
  Zhou et al. · *NeurIPS 2023* · 2023-02 · `📄 peer-reviewed` · 92 citations (S2)  
  [[Paper](https://arxiv.org/abs/2302.14040)]  
  Introduces permutation-equivariant neural functionals that process weights or gradients of MLPs and CNNs through NF-Layers with parameter sharing. Tasks include predicting generalization, producing winning-ticket sparsity masks, and classifying or editing implicit neural representations.

- **[Graph Metanetworks for Processing Diverse Neural Architectures](https://arxiv.org/abs/2312.04501)**  
  Lim et al. · *ICLR 2024* · 2023-12 · `📄 peer-reviewed` · 69 citations (S2)  
  [[Paper](https://arxiv.org/abs/2312.04501)]  
  Represents input networks as graphs and processes them with graph neural networks. Handles attention, normalization, convolutional and ResNet blocks, proves expressivity and equivariance to parameter permutation symmetries, and validates on several metanetwork tasks.

- **[Neural Decompiling of Tracr Transformers](https://arxiv.org/abs/2410.00061)**  
  Thurnherr, Riesen · *Preprint* · 2024-09 · `📝 preprint` · 3 citations (S2)  
  [[Paper](https://arxiv.org/abs/2410.00061)]  
  Generates a dataset of transformer-weight and RASP-program pairs with Tracr, then trains a model to recover RASP code from weights. Reproduces over 30% of test programs exactly; over 70% of outputs are functionally equivalent.

- **[A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090)**  
  Xiaolong Han et al. · *Preprint* · 2026-03-10 · `📝 preprint` · 26 citations (S2)  
  [[Paper](https://arxiv.org/abs/2603.10090)]  
  Taxonomy of learning on weights: geometry and symmetries, weight embeddings, and weight generation.

### Mechanistic interpretability that reads weights

- **[Visualizing and Understanding Convolutional Networks](https://arxiv.org/abs/1311.2901)**  
  NYU · *ECCV 2014* · 2013-11 · `📄 peer-reviewed` · 17.8k citations (S2)  
  [[Paper](https://arxiv.org/abs/1311.2901)]  
  Introduces a technique that projects activations back to pixels, plus an ablation study of layers. The diagnosis yields an architecture outperforming Krizhevsky et al. on ImageNet, and it beats prior results on Caltech-101 and Caltech-256 after softmax retraining.

- **[Zoom In: An Introduction to Circuits](https://distill.pub/2020/circuits/zoom-in/)**  
  OpenAI Clarity team · *Distill* · 2020 · `📄 peer-reviewed` · 853 citations (S2)  
  [[Paper](https://distill.pub/2020/circuits/zoom-in/)]  
  Claims that features connect into circuits by weights, and reads circuits directly from InceptionV1 weights. Opens the Distill Circuits thread from the OpenAI Clarity team in 2020, framing circuits as the unit of study.

- **[Transformer Feed-Forward Layers Are Key-Value Memories](https://arxiv.org/abs/2012.14913)**  
  Tel Aviv University / AI2 · *EMNLP 2021* · 2020-12 · `📄 peer-reviewed` · 1.8k citations (S2)  
  [[Paper](https://arxiv.org/abs/2012.14913)]  
  Shows that feed-forward layers act as key-value memories: keys correlate with textual patterns in training examples, and values induce output vocabulary distributions. Lower layers capture shallow patterns, upper layers more semantic ones; a layer's output composes its memories.

- **[Curve Circuits](https://distill.pub/2020/circuits/curve-circuits/)**  
  OpenAI · *Distill* · 2021 · `📄 peer-reviewed`  
  [[Paper](https://distill.pub/2020/circuits/curve-circuits/)]  
  Reverse-engineers the curve detection algorithm and uses its ideas to craft an artificial neural network from scratch that reimplements it. The page does not say whether every weight was set by hand.

- **[A Mathematical Framework for Transformer Circuits](https://transformer-circuits.pub/2021/framework/index.html)**  
  Anthropic · *Transformer Circuits thread* · 2021 · `💬 post only`  
  [[Post](https://transformer-circuits.pub/2021/framework/index.html)]  
  Defines QK circuits (W_E^T W_QK W_E) and OV circuits (W_U W_OV W_E) that can be read directly from weight matrices, and finds induction heads by reading composition between heads. Published by Anthropic in December 2021.

- **[In-context Learning and Induction Heads](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)**  
  Anthropic · *Transformer Circuits thread* · 2022 · `💬 post only` · 1.1k citations (S2)  
  [[Post](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html)]  
  Finds induction heads, attention-head circuits that complete repeated patterns in context, by reading the composition between heads, and argues they drive much of in-context learning.

- **[Toy Models of Superposition](https://transformer-circuits.pub/2022/toy_model/index.html)**  
  Anthropic · *Transformer Circuits thread* · 2022 · `💬 post only` · 1.2k citations (S2)  
  [[Post](https://transformer-circuits.pub/2022/toy_model/index.html)]  
  Explains polysemantic neurons through superposition, where a model represents more features than it has neurons. Anthropic work with Harvard collaborators, published in 2022 in the Transformer Circuits thread and as arXiv 2209.10652.

- **[Analyzing Transformers in Embedding Space](https://arxiv.org/abs/2209.02535)**  
  Tel Aviv University · *ACL 2023* · 2022-09 · `📄 peer-reviewed` · 161 citations (S2)  
  [[Paper](https://arxiv.org/abs/2209.02535)]  
  Interprets all parameters of a trained Transformer by projecting them into embedding space, with no forward or backward pass. Applications include aligning parameters across models and building a classifier without training by translating a fine-tuned classifier's parameters.

- **[Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small](https://arxiv.org/abs/2211.00593)**  
  Redwood Research · *ICLR 2023* · 2022-11 · `📄 peer-reviewed` · 1.4k citations (S2)  
  [[Paper](https://arxiv.org/abs/2211.00593)]  
  Explains how GPT-2 small performs indirect object identification with 26 attention heads in 7 main classes, found through causal interventions, and evaluates the explanation by faithfulness, completeness and minimality.

- **[Towards Monosemanticity: Decomposing Language Models With Dictionary Learning](https://transformer-circuits.pub/2023/monosemantic-features/index.html)**  
  Anthropic · *Transformer Circuits thread* · 2023 · `💬 post only`  
  [[Post](https://transformer-circuits.pub/2023/monosemantic-features/index.html)]  
  Decomposes a one-layer transformer's MLP activations into thousands of interpretable features with sparse dictionary learning, giving a feature basis in place of individual neurons.

- **[Progress Measures for Grokking via Mechanistic Interpretability](https://arxiv.org/abs/2301.05217)**  
  Nanda independent; Chan and Steinhardt at UC Berkeley · *ICLR 2023* · 2023-01 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.05217)]  
  Fully reverse engineers the algorithm small transformers learn for modular addition, which uses discrete Fourier transforms and trigonometric identities. Confirms it through activations, weights and ablations, and defines progress measures splitting training into memorization, circuit formation and cleanup.

- **[Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://arxiv.org/abs/2309.08600)**  
  Hoagy Cunningham et al. · *ICLR 2024* · 2023-09 · `📄 peer-reviewed` · 1.8k citations (S2)  
  [[Paper](https://arxiv.org/abs/2309.08600)]  
  Trains sparse autoencoders to reconstruct language-model activations, learning sparsely activating features that are more interpretable and monosemantic than alternatives by automated measures. Pinpoints features causally responsible for counterfactual behavior on indirect object identification more finely than prior decompositions.

- **[Interpretability in Parameter Space: Minimizing Mechanistic Description Length with Attribution-based Parameter Decomposition](https://arxiv.org/abs/2501.14926)**  
  Apollo Research · *Preprint* · 2025-01 · `📝 preprint` · 26 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.14926)]  
  Introduces Attribution-based Parameter Decomposition, which splits a network's parameters into components that are faithful, minimal in number per input, and maximally simple. Identifies ground-truth mechanisms in toy settings; scaling to non-toy models remains open.

### Activation steering

- **[Steering Language Models With Activation Engineering (ActAdd)](https://arxiv.org/abs/2308.10248)**  
  Alexander Matt Turner et al. · *Preprint* · 2023-08-20 · `📝 preprint` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2308.10248)]  
  Adds a direction computed from contrasting prompts to the residual stream at inference.

- **[Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405)**  
  Andy Zou et al. · *Preprint* · 2023-10-02 · `📝 preprint` · 1.6k citations (S2)  
  [[Paper](https://arxiv.org/abs/2310.01405)] [[Code](https://github.com/andyzoujm/representation-engineering)] ![GitHub stars](https://img.shields.io/github/stars/andyzoujm/representation-engineering?style=social)  
  Reads and controls high-level concepts through population-level directions in representations.

- **[Steering Llama 2 via Contrastive Activation Addition (CAA)](https://arxiv.org/abs/2312.06681)**  
  Nina Rimsky et al. · *ACL 2024* · 2023-12-09 · `📄 peer-reviewed` · 1.4k citations (S2)  
  [[Paper](https://arxiv.org/abs/2312.06681)]  
  Steering vectors from paired positive and negative examples shift behaviors such as sycophancy.

### Automated interpretability agents

- **[Network Dissection: Quantifying Interpretability of Deep Visual Representations](https://arxiv.org/abs/1704.05796)**  
  MIT CSAIL · *CVPR 2017* · 2017-04 · `📄 peer-reviewed` · 1.9k citations (S2)  
  [[Paper](https://arxiv.org/abs/1704.05796)]  
  Introduces a framework that scores individual hidden units of CNNs by their alignment with a dataset of semantic concepts, labelling units with objects, parts, scenes, textures, materials and colors. Compares networks across training tasks, initializations, depth, width, dropout and batch normalization.

- **[Natural Language Descriptions of Deep Visual Features](https://arxiv.org/abs/2201.11114)**  
  MIT · *ICLR 2022* · 2022-01 · `📄 peer-reviewed` · 173 citations (S2)  
  [[Paper](https://arxiv.org/abs/2201.11114)]  
  Introduces MILAN, which labels vision neurons with open-ended natural-language descriptions by searching for strings that maximize pointwise mutual information with the image regions where the neuron is active. Uses the descriptions to remove spurious-feature neurons.

- **[Language Models Can Explain Neurons in Language Models](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html)**  
  OpenAI · *OpenAI interactive paper* · 2023 · `💬 post only`  
  [[Post](https://openaipublic.blob.core.windows.net/neuron-explainer/paper/index.html)]  
  Has GPT-4 explain each GPT-2 XL MLP neuron, simulate its activations from that explanation, and score the match. Releases explanations for 307,200 neurons, over 1,000 scoring at least 0.8; the method works worse on larger models and later layers.

- **[Towards Automated Circuit Discovery for Mechanistic Interpretability](https://arxiv.org/abs/2304.14997)**  
  Independent research, UCL, Cambridge and others · *NeurIPS 2023* · 2023-04 · `📄 peer-reviewed` · 924 citations (S2)  
  [[Paper](https://arxiv.org/abs/2304.14997)]  
  Automates circuit discovery by pruning computational-graph edges whose patching barely changes the output. Rediscovers 5/5 component types in GPT-2 Small's Greater-Than circuit, selecting 68 of 32,000 edges, all found manually before.

- **[FIND: A Function Description Benchmark for Evaluating Interpretability Methods](https://arxiv.org/abs/2309.03886)**  
  MIT · *NeurIPS 2023* · 2023-09 · `📄 peer-reviewed` · 43 citations (S2)  
  [[Paper](https://arxiv.org/abs/2309.03886)]  
  Introduces FIND, a benchmark of functions resembling neural-network components, with paired descriptions, for evaluating automated interpretability methods. Also presents an Automated Interpretability Agent that generates function descriptions interactively, and evaluates language-model description methods.

- **[Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models](https://arxiv.org/abs/2401.06102)**  
  Google Research · *ICML 2024* · 2024-01 · `📄 peer-reviewed` · 296 citations (S2)  
  [[Paper](https://arxiv.org/abs/2401.06102)]  
  Introduces a framework in which a language model explains its own hidden representations in natural language. Treats prior vocabulary-projection and intervention methods as instances, and mitigates failures on early layers. Allows a larger model to explain a smaller one.

- **[A Multimodal Automated Interpretability Agent](https://arxiv.org/abs/2404.14394)**  
  MIT CSAIL · *ICML 2024* · 2024-04 · `📄 peer-reviewed` · 79 citations (S2)  
  [[Paper](https://arxiv.org/abs/2404.14394)]  
  Gives a pre-trained vision-language model tools to synthesize and edit inputs and compute maximally activating exemplars. Describes neurons comparably to expert human experimenters, reduces sensitivity to spurious features, and flags inputs likely to be misclassified.

- **[Automatically Interpreting Millions of Features in Large Language Models](https://arxiv.org/abs/2410.13928)**  
  EleutherAI · *ICML 2025* · 2024-10 · `📄 peer-reviewed` · 133 citations (S2)  
  [[Paper](https://arxiv.org/abs/2410.13928)]  
  Builds an open-source pipeline using LLMs to generate and score natural-language explanations for SAE features, with five new, cheaper scoring techniques including intervention scoring. Finds SAE latents much more interpretable than neurons, including sparsified ones.

- **[Building and Evaluating Alignment Auditing Agents](https://alignment.anthropic.com/2025/automated-auditing/)**  
  Anthropic · *Anthropic Alignment Science blog* · 2025 · `💬 post only`  
  [[Post](https://alignment.anthropic.com/2025/automated-auditing/)]  
  Builds alignment auditing agents, including a Claude Sonnet 4 investigator using SAE tools and steering. It solves the auditing game about 13% of the time, 42% with super-agent aggregation; interpretability tools raise win rates by roughly 10–20 points.

- **[Auditing Language Models for Hidden Objectives](https://arxiv.org/abs/2503.10965)**  
  Anthropic · *Preprint* · 2025-03 · `📝 preprint` · 91 citations (S2)  
  [[Paper](https://arxiv.org/abs/2503.10965)]  
  Trains a language model with a hidden objective of exploiting RLHF reward-model errors, then runs a blind auditing game with four teams. Three teams uncover the objective, using SAE interpretability, behavioral attacks and training data analysis.

- **[Learning to Interpret Weight Differences in Language Models](https://arxiv.org/abs/2510.05092)**  
  MIT · *Preprint* · 2025-10 · `📝 preprint` · 17 citations (S2)  
  [[Paper](https://arxiv.org/abs/2510.05092)]  
  Introduces Diff Interpretation Tuning, which trains an adapter on synthetic labeled weight diffs so a finetuned model describes its own finetuning-induced changes. Demonstrates it on reporting hidden behaviors and summarizing finetuned knowledge.

### Language-to-weights and LLM program search

- **[Evolution through Large Models](https://arxiv.org/abs/2206.08896)**  
  Joel Lehman et al. · *Preprint* · 2022-06 · `📝 preprint` · 191 citations (S2)  
  [[Paper](https://arxiv.org/abs/2206.08896)]  
  Uses a code-generating LLM as the mutation operator in genetic programming, combined with MAP-Elites. Produces hundreds of thousands of Python programs for ambulating robots in Sodarace, then uses them to train a conditional model that outputs walkers for a terrain.

- **[HyperTuning: Toward Adapting Large Language Models without Back-propagation](https://arxiv.org/abs/2211.12485)**  
  Jason Phang, Yi Mao, Pengcheng He, Weizhu Chen · *ICML 2023* · 2022-11 · `📄 peer-reviewed` · 61 citations (S2)  
  [[Paper](https://arxiv.org/abs/2211.12485)]  
  Trains a T5-based hypermodel, HyperT5, to generate soft prefixes or LoRA parameters for a frozen T5 model from few-shot examples, without backpropagation at adaptation. Evaluated on P3, MetaICL and Super-NaturalInstructions, it generates parameters for unseen tasks.

- **[Mathematical discoveries from program search with large language models](https://doi.org/10.1038/s41586-023-06924-6)**  
  Bernardino Romera-Paredes et al. · *Nature* · 2023 · `📄 peer-reviewed` · 1.6k citations (S2)  
  [[Paper](https://doi.org/10.1038/s41586-023-06924-6)]  
  Places an LLM inside an evolutionary loop where it proposes program mutations and an automated evaluator scores them. The system finds new cap-set constructions. Published in Nature by Google DeepMind authors.

- **[Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409)**  
  Chengrun Yang et al. · *ICLR 2024* · 2023-09 · `📄 peer-reviewed` · 1.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/2309.03409)]  
  Prompts an LLM with earlier solutions and their scores so it generates new ones. Tested on linear regression, traveling salesman and prompt optimization; best prompts beat human-designed ones by up to 8% on GSM8K and up to 50% on Big-Bench Hard.

- **[Large Language Models As Evolution Strategies](https://arxiv.org/abs/2402.18381)**  
  Robert Tjarko Lange, Yingtao Tian, Yujin Tang · *GECCO 2024 Companion* · 2024-02 · `📄 peer-reviewed` · 108 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.18381)]  
  Prompts an LLM zero-shot with sorted, discretized population members and asks it to propose an improved mean, forming an evolution strategy. It outperforms random search and Gaussian Hill Climbing on synthetic BBOB functions and small neuroevolution tasks.

- **[Transformer-Squared: Self-adaptive LLMs](https://arxiv.org/abs/2501.06252)**  
  Qi Sun, Edoardo Cetin, Yujin Tang · *ICLR 2025* · 2025-01 · `📄 peer-reviewed` · 22 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.06252)]  
  Adapts an LLM at inference in two passes: a dispatch system identifies task properties, then expert vectors trained with reinforcement learning, acting on singular components of weight matrices, are mixed. Reports outperforming LoRA with fewer parameters, including on vision-language tasks.

- **[NeuroGen: Neural Network Parameter Generation via Large Language Models](https://arxiv.org/abs/2505.12470)**  
  Jiaqi Wang, Yusen Zhang, Xi Li · *Preprint* · 2025-05 · `📝 preprint` · 3 citations (S2)  
  [[Paper](https://arxiv.org/abs/2505.12470)]  
  Generates neural network parameters with an LLM in two stages: pretraining on network checkpoints, then instruction tuning with prompts describing data, task and architecture. Reports that it generates usable network parameters.

- **[Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954)**  
  Jenny Zhang et al. · *Preprint* · 2025-05 · `📝 preprint` · 502 citations (S2)  
  [[Paper](https://arxiv.org/abs/2505.22954)]  
  Keeps an archive of coding agents, samples one, and has a foundation model produce a modified version that rewrites its own code. Each change is validated on coding benchmarks rather than proved, and SWE-bench performance increases.

- **[Text-to-LoRA: Instant Transformer Adaption](https://arxiv.org/abs/2506.06105)**  
  Rujikorn Charakorn, Edoardo Cetin, Yujin Tang, Robert Tjarko Lange · *ICML 2025* · 2025-06 · `📄 peer-reviewed` · 74 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.06105)]  
  Trains a hypernetwork to construct LoRA adapters for an LLM in one forward pass from a natural-language task description. Trained on 9 pre-trained LoRAs, its reconstructed adapters match task-specific adapters on test sets and generalize zero-shot to unseen tasks.

- **[AlphaEvolve: A coding agent for scientific and algorithmic discovery](https://arxiv.org/abs/2506.13131)**  
  Alexander Novikov et al. · *Preprint* · 2025-06 · `📝 preprint` · 1.2k citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.13131)]  
  Orchestrates LLMs in an evolutionary pipeline that improves algorithms by directly changing code, using feedback from evaluators. Applied to Google data-center scheduling and mathematics problems, it found a procedure multiplying two 4×4 complex matrices using 48 scalar multiplications.

- **[Self-Adapting Language Models](https://arxiv.org/abs/2506.10943)**  
  Adam Zweiger et al. · *NeurIPS 2025* · 2025-06 · `📄 peer-reviewed` · 103 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.10943)]  
  Has an LLM generate its own self-edits, meaning finetuning data and update directives, applied through supervised finetuning as persistent weight updates. A reinforcement learning loop rewards self-edits by downstream performance; tested on knowledge incorporation and few-shot generalization.

- **[Drag-and-Drop LLMs: Zero-Shot Prompt-to-Weights](https://arxiv.org/abs/2506.16406)**  
  Zhiyuan Liang et al. · *NeurIPS 2025* · 2025-06 · `📄 peer-reviewed` · 29 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.16406)]  
  Maps a handful of unlabeled task prompts to LoRA matrices using a text encoder and a hyper-convolutional decoder. Reports up to 12,000× lower overhead than full fine-tuning and average gains up to 30% over trained LoRAs on unseen benchmarks.

### Weight-level security and safety

- **[Fault Injection Attack on Deep Neural Network](https://doi.org/10.1109/ICCAD.2017.8203770)**  
  Yannan Liu, Lingxiao Wei, Bo Luo, Qiang Xu · *ICCAD 2017* · 2017 · `📄 peer-reviewed` · 247 citations (S2)  
  [[Paper](https://doi.org/10.1109/ICCAD.2017.8203770)]  
  Shows that faults injected into a network's parameters can force misclassification, including a single bias attack that changes one bias term.

- **[Bit-Flip Attack: Crushing Neural Network with Progressive Bit Search](https://arxiv.org/abs/1903.12269)**  
  Adnan Siraj Rakin, Zhezhi He, Deliang Fan · *ICCV 2019* · 2019-03 · `📄 peer-reviewed` · 370 citations (S2)  
  [[Paper](https://arxiv.org/abs/1903.12269)]  
  Proposes an attack that flips a few bits in DRAM-stored weights, using Progressive Bit Search that combines gradient ranking and progressive search. Drops ResNet-18 top-1 accuracy from 69.8% to 0.1% with 13 flips out of 93 million bits.

- **[Terminal Brain Damage: Exposing the Graceless Degradation in Deep Neural Networks Under Hardware Fault Attacks](https://arxiv.org/abs/1906.01017)**  
  Sanghyun Hong et al. · *USENIX Security 2019* · 2019-06 · `📄 peer-reviewed` · 292 citations (S2)  
  [[Paper](https://arxiv.org/abs/1906.01017)]  
  Studies bitwise corruptions on 19 DNN models across six architectures and three image tasks. Finds most models have at least one parameter whose bit-flip causes over 90% accuracy loss; Rowhammer drops accuracy up to 99%.

- **[Weight Poisoning Attacks on Pre-trained Models](https://arxiv.org/abs/2004.06660)**  
  Keita Kurita, Paul Michel, Graham Neubig · *ACL 2020* · 2020-04 · `📄 peer-reviewed` · 657 citations (S2)  
  [[Paper](https://arxiv.org/abs/2004.06660)]  
  Constructs weight poisoning attacks in which pre-trained weights carry backdoors that appear after fine-tuning, triggered by a keyword. Uses a regularization method called RIPPLe and an initialization called Embedding Surgery, tested on sentiment, toxicity and spam tasks.

- **[An Embarrassingly Simple Approach for Trojan Attack in Deep Neural Networks](https://arxiv.org/abs/2006.08131)**  
  Ruixiang Tang et al. · *KDD 2020* · 2020-06 · `📄 peer-reviewed` · 242 citations (S2)  
  [[Paper](https://arxiv.org/abs/2006.08131)]  
  Proposes a training-free trojan attack that inserts a tiny trojan module into a target model without changing the original parameters. Reports 100% attack success rate without affecting original-task accuracy, and evades state-of-the-art trojan detection algorithms.

- **[Handcrafted Backdoors in Deep Neural Networks](https://arxiv.org/abs/2106.04690)**  
  Sanghyun Hong, Nicholas Carlini, Alexey Kurakin · *NeurIPS 2022* · 2021-06 · `📄 peer-reviewed` · 108 citations (S2)  
  [[Paper](https://arxiv.org/abs/2106.04690)]  
  Introduces a handcrafted backdoor attack that directly manipulates a model's weights instead of poisoning training data. Keeps attack success rate above 96% across four datasets and four architectures, and evades many backdoor detection and removal defenses.

- **[Planting Undetectable Backdoors in Machine Learning Models](https://arxiv.org/abs/2204.06974)**  
  Shafi Goldwasser, Michael P. Kim, Vinod Vaikuntanathan, Or Zamir · *FOCS 2022* · 2022-04 · `📄 peer-reviewed` · 118 citations (S2)  
  [[Paper](https://arxiv.org/abs/2204.06974)]  
  Shows how a malicious learner can plant a backdoor that no computationally bounded observer can detect without the key. Gives a digital-signature construction for any model and a white-box undetectable construction for Random Fourier Features and random ReLU networks.

- **[Data-free Backdoor Removal based on Channel Lipschitzness](https://arxiv.org/abs/2208.03111)**  
  Runkai Zheng, Rongjun Tang, Jianze Li, Li Liu · *ECCV 2022* · 2022-08 · `📄 peer-reviewed` · 167 citations (S2)  
  [[Paper](https://arxiv.org/abs/2208.03111)]  
  Defines a Channel Lipschitz Constant and computes an upper bound directly from weight matrices. Prunes channels with high values to remove backdoors without data, reporting state-of-the-art results among mainstream defense methods.

- **[Assessing the Brittleness of Safety Alignment via Pruning and Low-Rank Modifications](https://arxiv.org/abs/2402.05162)**  
  Boyi Wei et al. · *ICML 2024* · 2024-02 · `📄 peer-reviewed` · 284 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.05162)]  
  Identifies safety-critical regions in LLMs through pruning and low-rank modifications, finding them sparse: about 3% at the parameter level and 2.5% at the rank level. Removing them compromises safety without significantly reducing utility.

- **[BadEdit: Backdooring Large Language Models by Model Editing](https://arxiv.org/abs/2403.13355)**  
  Yanzhou Li et al. · *ICLR 2024* · 2024-03 · `📄 peer-reviewed` · 163 citations (S2)  
  [[Paper](https://arxiv.org/abs/2403.13355)]  
  Formulates backdoor injection as a lightweight knowledge editing problem that directly alters a subset of LLM parameters. Needs 15 samples, reaches up to 100% attack success rate, and the backdoor survives later fine-tuning.

- **[Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717)**  
  Andy Arditi et al. · *NeurIPS 2024* · 2024-06-17 · `📄 peer-reviewed` · 1.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/2406.11717)]  
  Orthogonalizing weights against one direction removes refusal. It is the same kind of edit as the Qwen loop fix.

- **[PrisonBreak: Jailbreaking Large Language Models with at Most Twenty-Five Targeted Bit-flips](https://arxiv.org/abs/2412.07192)**  
  Zachary Coalson et al. · *Preprint* · 2024-12 · `📝 preprint` · 7 citations (S2)  
  [[Paper](https://arxiv.org/abs/2412.07192)]  
  Jailbreaks safety-aligned LLMs by flipping 5 to 25 targeted bits in parameters, using a bit-selection algorithm. Reaches 80-98% attack success on 10 open-source LLMs, and 69-91% on 5 models in a GDDR6 Rowhammer demonstration.

### Policy surgery, control and robot policies

- **[Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks](https://arxiv.org/abs/1702.01135)**  
  Guy Katz et al. · *CAV 2017* · 2017-02 · `📄 peer-reviewed` · 2.2k citations (S2)  
  [[Paper](https://arxiv.org/abs/1702.01135)]  
  Presents an SMT-based technique that extends the simplex method to handle ReLU activations, verifying properties of deep networks or giving counter-examples. Tested on ACAS Xu collision-avoidance networks, it proves properties of networks an order of magnitude larger than prior methods.

- **[Parameter Space Noise for Exploration](https://arxiv.org/abs/1706.01905)**  
  Matthias Plappert et al. · *ICLR 2018* · 2017-06 · `📄 peer-reviewed` · 709 citations (S2)  
  [[Paper](https://arxiv.org/abs/1706.01905)]  
  Adds noise directly to an agent's parameters rather than to its actions to drive exploration. Tested with DQN, DDPG and TRPO, it learns more efficiently than action-space noise and evolutionary strategies alone.

- **[Simple random search provides a competitive approach to reinforcement learning](https://arxiv.org/abs/1803.07055)**  
  Horia Mania, Aurelia Guy, Benjamin Recht · *NeurIPS 2018* · 2018-03 · `📄 peer-reviewed` · 340 citations (S2)  
  [[Paper](https://arxiv.org/abs/1803.07055)]  
  Introduces a random search method for training static linear policies for continuous control. It matches state-of-the-art sample efficiency on MuJoCo locomotion tasks and is at least 15 times more computationally efficient than the fastest competing model-free methods.

- **[Verifiable Reinforcement Learning via Policy Extraction](https://arxiv.org/abs/1805.08328)**  
  Osbert Bastani, Yewen Pu, Armando Solar-Lezama · *NeurIPS 2018* · 2018-05 · `📄 peer-reviewed` · 442 citations (S2)  
  [[Paper](https://arxiv.org/abs/1805.08328)]  
  Trains decision-tree policies guided by a DNN oracle and its Q-function, combining model compression with imitation learning. The trees are verified on Pong variants and cart-pole, and match the original DNN policy's performance.

- **[Efficient Representation and Approximation of Model Predictive Control Laws via Deep Learning](https://arxiv.org/abs/1806.10644)**  
  Benjamin Karg, Sergio Lucia · *IEEE Transactions on Cybernetics* · 2018-06 · `📄 peer-reviewed` · 315 citations (S2)  
  [[Paper](https://arxiv.org/abs/1806.10644)]  
  Shows that ReLU networks can exactly represent the piecewise affine function from model predictive control of linear time-invariant systems. Gives bounds on the minimum layers and neurons required, and illustrates smaller memory needs through simulation examples.

- **[Verisig: Verifying Safety Properties of Hybrid Systems with Neural Network Controllers](https://arxiv.org/abs/1811.01828)**  
  Radoslav Ivanov et al. · *HSCC 2019* · 2018-11 · `📄 peer-reviewed` · 303 citations (S2)  
  [[Paper](https://arxiv.org/abs/1811.01828)]  
  Converts sigmoid-based neural network controllers into equivalent hybrid systems, then checks closed-loop safety with reachability tools. Shows reachability is decidable for one-hidden-layer networks, and for general networks if Schanuel's conjecture holds. Evaluated in two case studies.

- **[Weight Agnostic Neural Networks](https://arxiv.org/abs/1906.04358)**  
  Adam Gaier, David Ha · *NeurIPS 2019* · 2019-06 · `📄 peer-reviewed` · 272 citations (S2)  
  [[Paper](https://arxiv.org/abs/1906.04358)]  
  Searches for network architectures that perform tasks without weight training, evaluating each with a single shared weight sampled from a uniform distribution. Finds minimal networks solving reinforcement learning tasks, and MNIST networks with accuracy well above chance.

- **[Dota 2 with Large Scale Deep Reinforcement Learning](https://arxiv.org/abs/1912.06680)**  
  Christopher Berner et al. · *Preprint* · 2019-12 · `📝 preprint` · 2.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/1912.06680)]  
  Trains OpenAI Five with self-play RL over 10 months and beats the Dota 2 world champions; over twenty offline surgeries change the live policy's architecture while preserving its function.

- **[Neural Network Surgery with Sets](https://arxiv.org/abs/1912.06719)**  
  Jonathan Raiman, Susan Zhang, Christy Dennison · *Preprint* · 2019-12 · `📝 preprint` · 6 citations (S2)  
  [[Paper](https://arxiv.org/abs/1912.06719)]  
  Formalizes surgery, the transfer of trained weights between networks across feature and architecture changes. Uses discrete feature sets and set operations to determine automatically which components to keep and which to retrain, validated on the OpenAI Five model.

- **[Rapidly Adaptable Legged Robots via Evolutionary Meta-Learning](https://arxiv.org/abs/2003.01239)**  
  Xingyou Song et al. · *IROS 2020* · 2020-03 · `📄 peer-reviewed` · 98 citations (S2)  
  [[Paper](https://arxiv.org/abs/2003.01239)]  
  Combines evolutionary-strategies meta-learning with a Batch Hill-Climbing adaptation operator to adapt robot policies to changed dynamics. On a quadruped, it adapts the policy using less than 3 minutes of real data.

- **[Reincarnating Reinforcement Learning: Reusing Prior Computation to Accelerate Progress](https://arxiv.org/abs/2206.01626)**  
  Rishabh Agarwal et al. · *NeurIPS 2022* · 2022-06 · `📄 peer-reviewed` · 102 citations (S2)  
  [[Paper](https://arxiv.org/abs/2206.01626)]  
  Proposes reincarnating RL, a workflow where prior computation such as learned policies is reused across design iterations or agents. Proposes an algorithm for transferring a sub-optimal policy to a value-based agent, tested on Atari 2600, locomotion and stratospheric balloon navigation.

- **[Mechanistic Interpretability for Steering Vision-Language-Action Models](https://arxiv.org/abs/2509.00328)**  
  Häon, Stocking, Chuang, Tomlin · *CoRL 2025* · 2025-08 · `📄 peer-reviewed` · 55 citations (S2)  
  [[Paper](https://arxiv.org/abs/2509.00328)] [[Code](https://github.com/vla-mech-interp/mechanistic-steering-vlas)] ![GitHub stars](https://img.shields.io/github/stars/vla-mech-interp/mechanistic-steering-vlas?style=social)  
  Steering OpenVLA and π0 through FFN value vectors shifts end-effector motion on LIBERO by 27.7% on average; only the low and slow steers held up on hardware.

- **[Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models](https://arxiv.org/abs/2603.19183)**  
  Swann, McGranahan, Buurmeijer, Kennedy, Schwager · *CoRL 2026* · 2026-03 · `📄 peer-reviewed` · 32 citations (S2)  
  [[Paper](https://arxiv.org/abs/2603.19183)] [[Code](https://github.com/swannaiden/drvla)] ![GitHub stars](https://img.shields.io/github/stars/swannaiden/drvla?style=social)  
  SAEs on π0.5 and OpenVLA: amplifying general features induces matching behavior and ablating them destroys performance, but most features are episode-specific memorization.

- **[Contrastive Conceptor Activation Steering (COAST): Unlocking Vision-Language-Action Models through Hidden States](https://arxiv.org/abs/2605.17144)**  
  Miranda Muqing Miao, Subin Kim, Brandon Yang, Lyle Ungar · *Preprint* · 2026-05 · `📝 preprint` · 9 citations (S2)  
  [[Paper](https://arxiv.org/abs/2605.17144)]  
  Training-free conceptor steering of a VLA's action-expert residual stream (GR00T N1.5), learned from a few success and failure rollouts.

- **[Robotic Policy Adaptation via Weight-Space Meta-Learning (WIZARD)](https://arxiv.org/abs/2606.07217)**  
  Christian Bianchi et al. · *Preprint* · 2026-06 · `📝 preprint` · 1 citations (S2)  
  [[Paper](https://arxiv.org/abs/2606.07217)]  
  A meta-network turns language and video into LoRA weights for a frozen VLA, with no test-time optimization.

- **[Steering Robustness into World Action Models via Mechanistic Interpretability and Optimal Control (WA-LQR)](https://arxiv.org/abs/2607.14943)**  
  *Preprint* · 2026-07 · `📝 preprint` · 8 citations (S2)  
  [[Paper](https://arxiv.org/abs/2607.14943)]  
  Closed-loop LQR activation steering of Cosmos-Policy, DiT4DiT and LingBot-VA under camera, gripper and noise perturbations. Linear separability predicts which models can be steered.

- **[DiMaS: Distribution Matching for Steering Vision-Language-Action Models](https://arxiv.org/abs/2607.14280)**  
  Khayatan, Meziane, Parekh, Cord · *Preprint* · 2026-07 · `📝 preprint` · 2 citations (S2)  
  [[Paper](https://arxiv.org/abs/2607.14280)] [[Code](https://github.com/pegah-kh/dimas)] ![GitHub stars](https://img.shields.io/github/stars/pegah-kh/dimas?style=social)  
  In flow-matching VLAs, behavioral features are linearly decodable but not linearly steerable, which motivates distribution matching instead.

- **[Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts (DART)](https://arxiv.org/abs/2607.00666)**  
  Taewook Kang, Taeheon Kim, Donghyun Shin, Jonghyun Choi · *Preprint* · 2026-07-01 · `📝 preprint` · 3 citations (S2)  
  [[Paper](https://arxiv.org/abs/2607.00666)]  
  Adapts a VLA to camera and embodiment shifts from one demonstration through weight-vector arithmetic with subspace alignment.

- **[Suppression Sticks, Locality Is Fragile: A Closed-Loop Audit of Task-Vector Negation in VLA Policies](https://arxiv.org/abs/2608.04692)**  
  Wang, Guo, Dai, Zhao, Guo, Xiong · *Preprint* · 2026-08 · `📝 preprint` · 1 citations (S2)  
  [[Paper](https://arxiv.org/abs/2608.04692)]  
  Subtracting per-skill task vectors on 10 LIBERO-Goal skills: 5 are cleanly suppressed, 3 resist and 2 collapse the policy. Unrelated tasks keep only 52% of their success on average, and cosine between task vectors does not predict the outcome.

- **[RoboIRS: Inference-Time Internal Representation Steering for Generalist Robot Policies](https://arxiv.org/abs/2610.04681)**  
  Lei, Liu, Li, Zhang, Liang, She et al. · *Preprint* · 2026-10 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.04681)] [[Project](https://rollingoat.github.io/roboirs/)]  
  Linear classifiers on success and failure rollouts pick intervention sites and directions in frozen policies. π0.5 on 15 LIBERO-PRO tasks: 44.4% to 66.2%; Cosmos Policy: 35.4% to 55.4%. A plain diff-of-means direction already reaches 62.6% on π0.5, the baseline any agent edit has to beat.

- **[Behavioral Steering of Vision-Language-Action Models in the Low-Parameter Regime](https://arxiv.org/abs/2611.00522)**  
  Tcheng, Zhu · *NeurIPS 2026 RoboPAD Workshop* · 2026-10 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2611.00522)]  
  TinyLoRA adapters of 8 to 384 parameters on a frozen OpenVLA-OFT, trained by GRPO or gradient-free CMA-ES. With 256 parameters carry height rises 120 mm at 92% success. The closest tiny-weight-edit baseline for an agent edit.

- **[Causal Analysis of Robot Foundation Models Enables Efficiency Gains](https://arxiv.org/abs/2610.20750)**  
  Swann, Papillon, Jacobs, Boppana, Haklay, Bigelow et al. · *Preprint* · 2026-10 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.20750)]  
  Activation patching on π0.5, MolmoAct2 and MolmoBot: information reaches the action expert through a narrow band of mid-to-late cross-attention layers, and patching there redirects which object is picked and where the arm moves. A map of where edits should land.

## 📖 Surveys and Reviews

*Surveys, reviews, tutorials, books and position papers of the fields that read, edit or write weights. None, to our knowledge, covers a general language model doing so.*

### Model and knowledge editing

- **[Where Does Knowledge Live? Representational, Causal, and Editable Localization in Language Models: A Survey](https://doi.org/10.20944/preprints202608.1605.v1)**  
  Zhuomin Chen et al. · *Preprints.org* · 2026-08 · `📝 preprint`  
  [[Paper](https://doi.org/10.20944/preprints202608.1605.v1)]  
  Separates three senses of knowledge localization in language models (representational, causal and editable) and reviews the evidence that they disagree: causal tracing can miss the best edit site and superposition makes single neurons polysemantic.

- **[Knowledge Mechanisms Across the Lifecycle of Large Language Models](https://doi.org/10.17605/osf.io/c8hxb)**  
  Hao Xiang et al. · *OSF Preprints* · 2026-07 · `📝 preprint`  
  [[Paper](https://doi.org/10.17605/osf.io/c8hxb)]  
  Traces how knowledge is acquired, represented, used, revised and transferred inside LLMs with a stage-driven taxonomy, moving from the model-as-knowledge-base view to micro-level mechanisms such as localization, superposition and knowledge conflict.

- **[Is Model Editing Built on Sand? Revealing Its Illusory Success and Fragile Foundation](https://arxiv.org/abs/2510.00625)**  
  Wei Liu et al. · *Preprint* · 2025-10 · `📝 preprint` · 7 citations (S2)  
  [[Paper](https://arxiv.org/abs/2510.00625)]  
  Argues that reported model editing success is illusory, with editors exploiting shortcuts instead of semantics, and introduces new evaluation methods showing state-of-the-art approaches collapse even under simple negation queries.

- **[A Dual-Axis Taxonomy of Knowledge Editing for LLMs: From Mechanisms to Functions](https://arxiv.org/abs/2508.08795)**  
  Amir Mohammad Salehoof et al. · *Preprint* · 2025-08 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2508.08795)]  
  Introduces a taxonomy of knowledge editing for LLMs along two axes: editing mechanism and the function of edited knowledge, spanning factual, temporal, conceptual, commonsense, and social knowledge, plus problem definition, evaluation tasks, and datasets.

- **[Editing Across Languages: A Survey of Multilingual Knowledge Editing](https://arxiv.org/abs/2505.14393)**  
  Nadir Durrani, Basel Mousi, Fahim Dalvi · *EMNLP 2025* · 2025-05 · `📄 peer-reviewed` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2505.14393)]  
  Surveys multilingual knowledge editing, organizing methods into parameter-based, memory-based, fine-tuning, and hypernetwork approaches, and reviewing benchmarks, transfer findings, cross-lingual propagation challenges, and open problems including language anisotropy, evaluation coverage, and edit scalability.

- **[Bring Your Own Knowledge: A Survey of Methods for LLM Knowledge Expansion](https://arxiv.org/abs/2502.12598)**  
  Mingyang Wang et al. · *Workshop* · 2025-02 · `📄 peer-reviewed` · 19 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.12598)]  
  Surveys methods for expanding LLM knowledge across factual information, domain expertise, language proficiency, and user preferences, covering continual learning, model editing, and retrieval-based adaptation, and discussing knowledge consistency and scalability challenges.

- **[Position: Editing Large Language Models Poses Serious Safety Risks](https://arxiv.org/abs/2502.02958)**  
  Paul Youssef et al. · *ICML 2025* · 2025-02 · `📄 peer-reviewed` · 27 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.02958)]  
  Argues that editing LLMs poses overlooked safety risks, citing malicious use cases, ecosystem vulnerabilities, and low institutional awareness, and calls for tamper-resistant models, countermeasures, and securing the AI ecosystem.

- **[The Mirage of Model Editing: Revisiting Evaluation in the Wild](https://arxiv.org/abs/2502.11177)**  
  Wanli Yang et al. · *ACL 2025* · 2025-02 · `📄 peer-reviewed` · 34 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.11177)]  
  Revisits model editing evaluation with the QAEdit benchmark and WILD framework, showing that single-edit performance drops from 96.8% to 38.5% under realistic testing and that sequential editing fails drastically at 1000 edits.

- **[Knowledge Mechanisms in Large Language Models: A Survey and Perspective](https://arxiv.org/abs/2407.15017)**  
  Mengru Wang et al. · *Findings of EMNLP 2024* · 2024-07 · `📄 peer-reviewed` · 82 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.15017)]  
  Reviews knowledge mechanisms in LLMs through a taxonomy of knowledge utilization (memorization, comprehension and application, creation) and knowledge evolution in individual and group models, and discusses the fragility of parametric knowledge and potential dark knowledge.

- **[Editing the Mind of Giants: An In-Depth Exploration of Pitfalls of Knowledge Editing in Large Language Models](https://arxiv.org/abs/2406.01436)**  
  Cheng-Hsun Hsueh et al. · *Findings of EMNLP 2024* · 2024-06 · `📄 peer-reviewed` · 15 citations (S2)  
  [[Paper](https://arxiv.org/abs/2406.01436)]  
  Surveys side effects of knowledge editing in LLMs, such as knowledge distortion and loss of general abilities, re-evaluating methods with consistent metrics and benchmarks and reviewing related work and research directions.

- **[Fundamental Problems With Model Editing: How Should Rational Belief Revision Work in LLMs?](https://arxiv.org/abs/2406.19354)**  
  Peter Hase et al. · *TMLR* · 2024-06 · `📄 peer-reviewed` · 38 citations (S2)  
  [[Paper](https://arxiv.org/abs/2406.19354)]  
  Critiques the standard formulation of model editing as belief revision, describing 12 open problems in problem definition, benchmarks, and editable beliefs, and proposes a semi-synthetic Wikidata testbed evaluated against an idealized Bayesian agent.

- **[Towards Lifelong Learning of Large Language Models: A Survey](https://arxiv.org/abs/2406.06391)**  
  Junhao Zheng et al. · *ACM Computing Surveys* · 2024-06 · `📄 peer-reviewed` · 121 citations (S2)  
  [[Paper](https://arxiv.org/abs/2406.06391)]  
  Surveys lifelong learning for LLMs, splitting strategies into internal knowledge (continual pretraining and finetuning) and external knowledge (retrieval-based and tool-based), with a taxonomy of 12 scenarios and emerging techniques like model expansion and data selection.

- **[Knowledge Conflicts for LLMs: A Survey](https://arxiv.org/abs/2403.08319)**  
  Rongwu Xu et al. · *EMNLP 2024* · 2024-03 · `📄 peer-reviewed` · 418 citations (S2)  
  [[Paper](https://arxiv.org/abs/2403.08319)]  
  Surveys knowledge conflicts in LLMs across three categories: context-memory, inter-context, and intra-memory conflict, examining their causes, model behaviors under conflict, and available solutions for improving robustness.

- **[Continual Learning for Large Language Models: A Survey](https://arxiv.org/abs/2402.01364)**  
  Wu et al. · *Preprint* · 2024-02 · `📄 peer-reviewed` · 205 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.01364)]  
  Surveys continual learning for LLMs through a multi-stage categorization of continual pretraining, instruction tuning, and alignment, contrasting it with simpler adaptation, retrieval-augmented generation, and model editing, and discussing benchmarks, challenges, and future directions.

- **[A Comprehensive Study of Knowledge Editing for Large Language Models](https://arxiv.org/abs/2401.01286)**  
  Ningyu Zhang et al. · *Preprint* · 2024-01 · `📝 preprint` · 194 citations (S2)  
  [[Paper](https://arxiv.org/abs/2401.01286)]  
  Reviews knowledge editing approaches for LLMs under a three-group categorization: using external knowledge, merging knowledge into the model, and editing intrinsic knowledge. Adds the KnowEdit benchmark for empirical evaluation and an analysis of knowledge location.

- **[Knowledge Editing for Large Language Models](https://aclanthology.org/2024.lrec-tutorials.6)**  
  Ningyu Zhang, Yunzhi Yao, Shumin Deng · *LREC-COLING 2024 tutorials* · 2024 · `📄 peer-reviewed` · 11 citations (S2)  
  [[Paper](https://aclanthology.org/2024.lrec-tutorials.6)]  
  Presents a tutorial on knowledge editing for large language models, serving as an introduction to the topic of modifying what a model knows after it has been trained.

- **[Trends in Integration of Knowledge and Large Language Models: A Survey and Taxonomy of Methods, Benchmarks, and Applications](https://arxiv.org/abs/2311.05876)**  
  Zhangyin Feng et al. · *Preprint* · 2023-11 · `📝 preprint` · 57 citations (S2)  
  [[Paper](https://arxiv.org/abs/2311.05876)]  
  Reviews how knowledge is integrated into LLMs through knowledge editing and retrieval augmentation, presenting a taxonomy of methods, benchmarks, and applications, along with analysis of methods and future research directions.

- **[Knowledge Editing for Large Language Models: A Survey](https://arxiv.org/abs/2310.16218)**  
  Song Wang et al. · *ACM Computing Surveys* · 2023-10 · `📄 peer-reviewed` · 299 citations (S2)  
  [[Paper](https://arxiv.org/abs/2310.16218)]  
  Reviews knowledge-based model editing for LLMs, formalizing the problem and organizing methods in a taxonomy based on how new knowledge is introduced, then covering metrics, datasets, and applications.

- **[A Survey on Knowledge Editing of Neural Networks](https://arxiv.org/abs/2310.19704)**  
  Vittorio Mazzia et al. · *IEEE TNNLS* · 2023-10 · `📄 peer-reviewed` · 55 citations (S2)  
  [[Paper](https://arxiv.org/abs/2310.19704)]  
  Reviews knowledge editing for neural networks, formalizing the problem in a common framework, distinguishing it from continual learning, and surveying the main editing approaches and datasets proposed so far.

- **[Emptying the Ocean with a Spoon: Should We Edit Models?](https://arxiv.org/abs/2310.11958)**  
  Yuval Pinter, Michael Elhadad · *Findings of EMNLP 2023* · 2023-10 · `📄 peer-reviewed` · 33 citations (S2)  
  [[Paper](https://arxiv.org/abs/2310.11958)]  
  Argues that direct model editing cannot be trusted as a systematic remedy for LLM factual errors, contrasting it with retrieval-based architectures, concept erasure, and attribution methods, and calls for cautious, limited use.

- **[Unveiling the Pitfalls of Knowledge Editing for Large Language Models](https://arxiv.org/abs/2310.02129)**  
  Zhoubo Li et al. · *ICLR 2024* · 2023-10 · `📄 peer-reviewed` · 51 citations (S2)  
  [[Paper](https://arxiv.org/abs/2310.02129)]  
  Investigates side effects of knowledge editing in LLMs using new benchmark datasets and metrics, identifying knowledge conflict from logically clashing edits and knowledge distortion of the model's innate knowledge structure.

- **[On Knowledge Editing in Federated Learning: Perspectives, Challenges, and Future Directions](https://arxiv.org/abs/2306.01431)**  
  Leijie Wu et al. · *Preprint* · 2023-06 · `📝 preprint` · 5 citations (S2)  
  [[Paper](https://arxiv.org/abs/2306.01431)]  
  Surveys knowledge editing, covering augmentation and removal, in federated learning, proposing a Federated Editable Learning paradigm across the FL lifecycle, placing existing methods within it, and outlining challenges and future directions.

- **[Editing Large Language Models: Problems, Methods, and Opportunities](https://arxiv.org/abs/2305.13172)**  
  Yunzhi Yao et al. · *EMNLP 2023* · 2023-05 · `📄 peer-reviewed` · 516 citations (S2)  
  [[Paper](https://arxiv.org/abs/2305.13172)]  
  Surveys model editing for LLMs, defining the task and its challenges, empirically comparing leading methods, and introducing a new benchmark dataset to evaluate editing techniques and guide method selection for specific tasks.

- **[Editing Large Language Models](https://aclanthology.org/2023.ijcnlp-tutorials.4.pdf)**  
  zjunlp group · *AACL-IJCNLP 2023 tutorial* · 2023 · `📄 peer-reviewed` · 5 citations (S2)  
  [[Paper](https://aclanthology.org/2023.ijcnlp-tutorials.4.pdf)]  
  Presents a three-hour tutorial on editing large language models, introducing the practice of modifying the behavior and knowledge of an already trained model.

### Model merging and weight arithmetic

- **[From Parameters to Behaviors: A Survey of Model Fusion for Large Language Models](https://arxiv.org/abs/2609.19553)**  
  Shuo Cai et al. · *Findings of EMNLP 2026* · 2026-09 · `📄 peer-reviewed` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2609.19553)]  
  Defines model fusion for LLMs and organizes prior work into parameter-level, representation-level, and behavior-level fusion. Also reviews metrics, benchmarks, applications, challenges, and future directions.

- **[Model Merging in the Era of Large Language Models: Methods, Applications, and Future Directions](https://arxiv.org/abs/2603.09938)**  
  Mingyang Song, Mao Zheng · *Preprint* · 2026-03 · `📝 preprint` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2603.09938)]  
  Surveys merging of fine-tuned LLMs through the FUSE taxonomy of foundations, unification strategies, scenarios, and ecosystem. Covers weight averaging, task vector arithmetic, sparsification, mixture-of-experts, evolutionary optimization, applications, tools, and benchmarks.

- **[A Short Survey of Averaging Techniques in Stochastic Gradient Methods](https://arxiv.org/abs/2603.09634)**  
  K. Lakshmanan · *Preprint* · 2026-03 · `📝 preprint` · 2 citations (S2)  
  [[Paper](https://arxiv.org/abs/2603.09634)]  
  Surveys averaging techniques in stochastic gradient optimization, from the theory of Polyak–Ruppert averaging to tail averaging, exponential moving averages, and stochastic weight averaging. Covers modern developments, machine learning applications, finite-sample results, and open problems.

- **[A Unified Study of LoRA Variants: Taxonomy, Review, Codebase, and Empirical Evaluation](https://arxiv.org/abs/2601.22708)**  
  Haonan He et al. · *Preprint* · 2026-01 · `📝 preprint` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2601.22708)]  
  Presents a unified study of LoRA variants, categorizing them along four axes: rank, optimization dynamics, initialization, and mixture-of-experts integration. Adds a theoretical review, a modular codebase, and a large-scale evaluation across language and image tasks.

- **[From Task-Specific Models to Unified Systems: A Review of Model Merging Approaches](https://arxiv.org/abs/2503.08998)**  
  Wei Ruan et al. · *Preprint* · 2025-03 · `📝 preprint` · 15 citations (S2)  
  [[Paper](https://arxiv.org/abs/2503.08998)]  
  Reviews model merging methods, establishing a new taxonomy and systematically comparing approaches, motivated by inconsistent terminology and settings where training data is inaccessible. Aims to give newcomers a structured overview of key developments.

- **[Harnessing Multiple Large Language Models: A Survey on LLM Ensemble](https://arxiv.org/abs/2502.18036)**  
  Zhijun Chen et al. · *IJCAI* · 2025-02 · `📄 peer-reviewed` · 137 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.18036)]  
  Reviews LLM ensemble methods, introducing a taxonomy and classifying approaches as ensemble-before-inference, ensemble-during-inference, or ensemble-after-inference. Also covers benchmarks, applications, and future research directions.

- **[Low-Rank Adaptation for Foundation Models: A Comprehensive Review](https://arxiv.org/abs/2501.00365)**  
  Menglin Yang et al. · *Preprint* · 2025-01 · `📝 preprint` · 67 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.00365)]  
  Reviews low-rank adaptation for foundation models beyond LLMs, covering technique foundations, emerging frontiers, and applications across multiple domains. Discusses challenges in theoretical understanding, scalability, and robustness.

- **[Deep Model Merging: The Sister of Neural Network Interpretability -- A Survey](https://arxiv.org/abs/2410.12927)**  
  Arham Khan et al. · *Preprint* · 2024-10 · `📝 preprint` · 1 citations (S2)  
  [[Paper](https://arxiv.org/abs/2410.12927)]  
  Surveys model merging through the lens of loss landscape geometry, distilling four characteristics: mode convexity, determinism, directedness, and connectivity. Argues these insights apply to interpretability and robustness, and proposes research directions at their intersection.

- **[Model Merging in LLMs, MLLMs, and Beyond: Methods, Theories, Applications and Opportunities](https://arxiv.org/abs/2408.07666)**  
  Enneng Yang et al. · *ACM Computing Surveys* · 2024-08 · `📄 peer-reviewed` · 337 citations (S2)  
  [[Paper](https://arxiv.org/abs/2408.07666)]  
  Surveys model merging across methods, theories, and applications, proposing a taxonomy of merging methods and covering use in LLMs, multimodal LLMs, and over ten machine learning subfields, with challenges and future directions.

- **[A Survey on Model MoErging: Recycling and Routing Among Specialized Experts for Collaborative Learning](https://arxiv.org/abs/2408.07057)**  
  Prateek Yadav et al. · *Preprint* · 2024-08 · `📝 preprint` · 78 citations (S2)  
  [[Paper](https://arxiv.org/abs/2408.07057)]  
  Surveys methods that recycle specialized expert models through routers, proposing a taxonomy of key design choices and suitable applications. Also inventories software tools and applications, and relates MoErging to model merging, multitask learning, and mixture-of-experts.

- **[Merge, Ensemble, and Cooperate! A Survey on Collaborative Strategies in the Era of Large Language Models](https://arxiv.org/abs/2407.06089)**  
  Jinliang Lu et al. · *Preprint* · 2024-07 · `📝 preprint` · 72 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.06089)]  
  Surveys collaborative strategies for LLMs, categorized into merging in parameter space, ensembling model outputs, and cooperation among models for specific tasks, and discusses motivations, applications, and future research directions.

- **[A Survey on LoRA of Large Language Models](https://arxiv.org/abs/2407.11046)**  
  Yuren Mao et al. · *Frontiers of Computer Science* · 2024-07 · `📄 peer-reviewed` · 203 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.11046)]  
  Reviews LoRA for large language models, categorizing progress into downstream adaptation variants, cross-task generalization by mixing multiple LoRA plugins, efficiency improvements, federated privacy-preserving methods, and applications. Also discusses future directions.

- **[Deep Model Fusion: A Survey](https://arxiv.org/abs/2309.15698)**  
  Weishi Li et al. · *IEEE TNNLS* · 2023-09 · `📄 peer-reviewed` · 140 citations (S2)  
  [[Paper](https://arxiv.org/abs/2309.15698)]  
  Surveys deep model fusion in four categories: mode connectivity, alignment, weight averaging, and ensemble learning, and analyzes challenges of fusing large-scale models such as high computational cost and interference between heterogeneous models.

### Steering, representation engineering and unlearning

- **[Machine Unlearning for Large Language Models: Foundations, Advances, and Agentic Extensions](https://arxiv.org/abs/2609.30909)**  
  Xiaoyu Xu et al. · *Preprint* · 2026-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.30909)]  
  Compares machine unlearning methods, benchmarks, and evidence across LLMs and systems with retrieval, memory, tools, and agents. Organizes them with a five-layer framework, seven-stage lifecycle, and six evidence dimensions, and argues current evidence is insufficient to establish removal.

- **[Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks](https://arxiv.org/abs/2607.07907)**  
  Sarwar et al. · *Findings of ACL 2026* · 2026-07 · `📄 peer-reviewed` · 10 citations (S2)  
  [[Paper](https://arxiv.org/abs/2607.07907)]  
  Surveys unlearning in multimodal foundation models across vision, language, audio and video, offering a system-oriented view. Provides a taxonomy comparing architectures and modalities by trade-offs among deletion strength, retention, efficiency, reversibility and robustness, and notes open problems.

- **[Position: The Term "Machine Unlearning" Is Overused in LLMs](https://arxiv.org/abs/2606.27379)**  
  Yoon, Jun, No · *ICML 2026* · 2026-06 · `📄 peer-reviewed` · 5 citations (S2)  
  [[Paper](https://arxiv.org/abs/2606.27379)]  
  Argues that "machine unlearning" is overused in LLM research and should be reserved for dataset-defined deletion approximating retraining without a specified forget set. Contends that refusal, entity removal and suppression need different terminology and evaluations matching their objectives.

- **[Is your algorithm unlearning or untraining?](https://arxiv.org/abs/2604.07962)**  
  Triantafillou et al. · *Preprint* · 2026-04 · `📄 peer-reviewed` · 6 citations (S2)  
  [[Paper](https://arxiv.org/abs/2604.07962)]  
  Argues that "unlearning" is overloaded across two problem formulations, distinguishing untraining, which reverses the influence of a forget set, from unlearning, which removes the broader underlying concept or behaviour. Gives technical definitions and maps literature settings to each.

- **[Unlearning in LLMs: Methods, Evaluation, and Open Challenges](https://arxiv.org/abs/2601.13264)**  
  Tyler Lizzo, Larry Heck · *Preprint* · 2026-01 · `📝 preprint` · 1 citations (S2)  
  [[Paper](https://arxiv.org/abs/2601.13264)]  
  Surveys unlearning methods for LLMs, categorized as data-centric, parameter-centric, architecture-centric, hybrid, and other strategies. Reviews benchmarks, metrics, and datasets, and outlines open problems including efficiency, formal guarantees, multimodal unlearning, and adversarial relearning.

- **[A Survey on Unlearning in Large Language Models](https://arxiv.org/abs/2510.25117)**  
  Ruichen Qiu et al. · *Preprint* · 2025-10 · `📝 preprint` · 7 citations (S2)  
  [[Paper](https://arxiv.org/abs/2510.25117)]  
  Reviews over 180 papers on LLM unlearning published since 2021, with a taxonomy by pipeline phase separating parameter modification from parameter selection. Analyzes evaluation, comparing 18 benchmarks and dividing memorization metrics into 10 categories.

- **[A Survey on Training-free Alignment of Large Language Models](https://arxiv.org/abs/2508.09016)**  
  Birong Pan et al. · *Findings of EMNLP 2025* · 2025-08 · `📄 peer-reviewed` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2508.09016)]  
  Reviews training-free alignment of LLMs, categorizing methods by pre-decoding, in-decoding, and post-decoding stages, examined for both LLMs and multimodal LLMs. Identifies key challenges and future directions.

- **[Generative Model Unlearning: A Survey through Target Events, Unlearning Operators, and Evaluation Protocols](https://arxiv.org/abs/2507.19894)**  
  Feng et al. · *Preprint* · 2025-07 · `📄 peer-reviewed` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2507.19894)]  
  Reviews generative model unlearning by formulating it as target-constrained distributional projection, where a target event, an unlearning operator and evidence on suppression, preservation and cost define a request. Reorganizes prior studies under this view.

- **[SoK: Machine Unlearning for Large Language Models](https://arxiv.org/abs/2506.09227)**  
  Jie Ren et al. · *Preprint* · 2025-06 · `📝 preprint` · 14 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.09227)]  
  Proposes an intention-oriented taxonomy of LLM unlearning, distinguishing true removal of internal knowledge from suppression of behavioral effects. Examines evaluation limitations and practical challenges such as scalability and sequential unlearning.

- **[Towards Reliable Forgetting: A Survey on Machine Unlearning Verification](https://arxiv.org/abs/2506.15115)**  
  Xue et al. · *ACM Computing Surveys 2026* · 2025-06 · `📄 peer-reviewed` · 19 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.15115)]  
  Surveys methods for verifying machine unlearning, proposing a taxonomy of behavioral verification and parametric verification based on the type of evidence used. Examines assumptions, strengths and limitations of representative methods, identifies deployment vulnerabilities, and lists open problems.

- **[Erasing Concepts, Steering Generations: A Comprehensive Survey of Concept Suppression](https://arxiv.org/abs/2505.19398)**  
  Yiwei Xie, Ping Liu, Zheng Zhang · *Preprint* · 2025-05 · `📝 preprint` · 13 citations (S2)  
  [[Paper](https://arxiv.org/abs/2505.19398)]  
  Surveys concept erasure in text-to-image diffusion models, organizing approaches along intervention level, optimization structure, and semantic scope. Discusses evaluation benchmarks, metrics, datasets, trade-offs, and future directions such as adversarial robustness.

- **[A Comprehensive Survey of Machine Unlearning Techniques for Large Language Models](https://arxiv.org/abs/2503.01854)**  
  Jiahui Geng et al. · *Preprint* · 2025-03 · `📝 preprint` · 43 citations (S2)  
  [[Paper](https://arxiv.org/abs/2503.01854)]  
  Surveys machine unlearning for LLMs, introducing definitions, paradigms, and a taxonomy of existing studies. Categorizes approaches by strengths and limitations, reviews evaluation metrics and benchmarks, and outlines future research directions.

- **[Taxonomy, Opportunities, and Challenges of Representation Engineering for Large Language Models](https://arxiv.org/abs/2502.19649)**  
  Jan Wehner et al. · *TMLR* · 2025-02 · `📄 peer-reviewed` · 45 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.19649)]  
  Surveys representation engineering for LLMs, which manipulates internal representations to control behavior, framing it as a pipeline of representation identification, operationalization, and control. Compares strengths and weaknesses, identifies challenges, and offers best-practice guidance.

- **[Representation Engineering for Large-Language Models: Survey and Research Challenges](https://arxiv.org/abs/2502.17601)**  
  Lukasz Bartoszcze et al. · *Preprint* · 2025-02 · `📝 preprint` · 29 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.17601)]  
  Formalizes the goals and methods of representation engineering, which uses contrasting inputs to detect and edit high-level concept representations in LLMs. Compares it with mechanistic interpretability, prompt engineering, and fine-tuning, outlines risks, and sets a research agenda.

- **[A Comprehensive Survey on Concept Erasure in Text-to-Image Diffusion Models](https://arxiv.org/abs/2502.14896)**  
  Changhoon Kim, Yanjun Qi · *Preprint* · 2025-02 · `📝 preprint` · 13 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.14896)]  
  Surveys concept erasure in text-to-image diffusion models, categorizing methods as fine-tuning for parameter updates, closed-form edits, or inference-time interventions, and by the architectural components they modify. Also covers adversarial attacks, defenses, datasets, metrics, and benchmarks.

- **[Position: Bridge the Gaps between Machine Unlearning and AI Regulation](https://arxiv.org/abs/2502.12430)**  
  Marino et al. · *NeurIPS 2025* · 2025-02 · `📄 peer-reviewed` · 9 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.12430)]  
  Argues that machine unlearning's usefulness for AI regulation depends on researchers closing gaps between current methods and applications, using the EU AI Act as a case study. Catalogs potential compliance applications and flags the technical gaps for each.

- **[Open Problems in Machine Unlearning for AI Safety](https://arxiv.org/abs/2501.04952)**  
  Barez et al. · *Preprint* · 2025-01 · `📄 peer-reviewed` · 67 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.04952)]  
  Identifies open problems in using machine unlearning for AI safety, focusing on dual-use knowledge in domains such as cybersecurity and CBRN. Covers side effects of removing dangerous knowledge, tensions with existing safety mechanisms, and challenges in evaluation and robustness.

- **[Machine Unlearning Doesn't Do What You Think: Lessons for Generative AI Policy and Research](https://arxiv.org/abs/2412.06966)**  
  Cooper et al. · *NeurIPS 2025* · 2024-12 · `📄 peer-reviewed` · 20 citations (S2)  
  [[Paper](https://arxiv.org/abs/2412.06966)]  
  Argues that machine unlearning does not deliver what policy discussions expect for generative AI, offering a framework for researchers and policymakers. Identifies mismatches between unlearning goals, removing information from parameters or suppressing it in outputs, and feasible implementations.

- **[Position: LLM Unlearning Benchmarks are Weak Measures of Progress](https://arxiv.org/abs/2410.02879)**  
  Thaker et al. · *SaTML 2025* · 2024-10 · `📄 peer-reviewed` · 76 citations (S2)  
  [[Paper](https://arxiv.org/abs/2410.02879)]  
  Argues that LLM unlearning benchmarks give an overly optimistic view of method effectiveness. Shows through simple benign modifications to popular benchmarks that supposedly unlearned information remains accessible or retained performance degrades, and recommends cautious interpretation and better future practice.

- **[Controllable Text Generation for Large Language Models: A Survey](https://arxiv.org/abs/2408.12599)**  
  Xun Liang et al. · *Preprint* · 2024-08 · `📝 preprint` · 93 citations (S2)  
  [[Paper](https://arxiv.org/abs/2408.12599)]  
  Reviews controllable text generation for LLMs, dividing tasks into content control and attribute control. Covers retraining, fine-tuning, reinforcement learning, prompt engineering, latent space manipulation, and decoding-time intervention, plus evaluation, applications, and challenges.

- **[Preserving Privacy in Large Language Models: A Survey on Current Threats and Solutions](https://arxiv.org/abs/2408.05212)**  
  Miranda et al. · *TMLR 2025* · 2024-08 · `📄 peer-reviewed` · 33 citations (S2)  
  [[Paper](https://arxiv.org/abs/2408.05212)]  
  Surveys privacy threats to LLMs, reviewing privacy attacks and the memorization of sensitive information. Organizes solutions along the learning pipeline, from dataset anonymization to differential privacy during training or inference and machine unlearning after training.

- **[Machine Unlearning in Generative AI: A Survey](https://arxiv.org/abs/2407.20516)**  
  Zheyuan Liu et al. · *Preprint* · 2024-07 · `📝 preprint` · 77 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.20516)]  
  Surveys machine unlearning in generative AI, spanning language and vision generative models, with a new problem formulation, evaluation methods, and structured discussion of the advantages and limitations of different technique types. Presents challenges and directions.

- **[Digital Forgetting in Large Language Models: A Survey of Unlearning Methods](https://arxiv.org/abs/2404.02062)**  
  Alberto Blanco-Justicia et al. · *Artificial Intelligence Review 58, art.* · 2024-04 · `📄 peer-reviewed` · 74 citations (S2)  
  [[Paper](https://arxiv.org/abs/2404.02062)]  
  Surveys digital forgetting in LLMs, covering background, motivations, desired properties, and a detailed taxonomy of machine unlearning methods. Also details datasets, models, and metrics for evaluating forgetting, retention, and runtime, and discusses challenges.

- **[Machine Unlearning for Traditional Models and Large Language Models: A Short Survey](https://arxiv.org/abs/2404.01206)**  
  Yi Xu · *Preprint* · 2024-04 · `📄 peer-reviewed` · 19 citations (S2)  
  [[Paper](https://arxiv.org/abs/2404.01206)]  
  Surveys machine unlearning for traditional models and LLMs, covering definitions, classification, evaluation criteria and challenges in different settings. Categorizes unlearning for each model type and proposes ways to measure effectiveness and efficiency.

- **[The Frontier of Data Erasure: Machine Unlearning for Large Language Models](https://arxiv.org/abs/2403.15779)**  
  Qu et al. · *Preprint* · 2024-03 · `📄 peer-reviewed` · 27 citations (S2)  
  [[Paper](https://arxiv.org/abs/2403.15779)]  
  Reviews machine unlearning for large language models, presenting methods for targeted forgetting without full retraining. Divides existing research into unlearning from unstructured textual data and from structured classification data, and discusses challenges in preserving model integrity.

- **[Rethinking Machine Unlearning for Large Language Models](https://arxiv.org/abs/2402.08787)**  
  Sijia Liu et al. · *Nature Machine Intelligence* · 2024-02 · `📄 peer-reviewed` · 383 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.08787)]  
  Explores machine unlearning for LLMs across conceptual formulation, methodologies, metrics, and applications, highlighting unlearning scope, data-model interaction, and multifaceted efficacy assessment. Connects it to model editing and influence functions, and outlines an assessment framework.

- **[Eight Methods to Evaluate Robust Unlearning in LLMs](https://arxiv.org/abs/2402.16835)**  
  Lynch et al. · *Preprint* · 2024-02 · `📄 peer-reviewed` · 185 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.16835)]  
  Surveys techniques and limitations of existing LLM unlearning evaluations, then applies a set of robustness tests to the Who's Harry Potter model. Finds extractable knowledge, comparable latent representations and collateral unlearning, arguing for comprehensive rather than ad-hoc evaluation.

- **[Knowledge Unlearning for LLMs: Tasks, Methods, and Challenges](https://arxiv.org/abs/2311.15766)**  
  Nianwen Si et al. · *Preprint* · 2023-11 · `📝 preprint` · 48 citations (S2)  
  [[Paper](https://arxiv.org/abs/2311.15766)]  
  Surveys knowledge unlearning for LLMs, defining the problem and categorizing methods into parameter optimization, parameter merging, and in-context learning. Presents evaluation datasets and concludes with ongoing challenges and future directions.

- **[Right to be Forgotten in the Era of Large Language Models: Implications, Challenges, and Solutions](https://arxiv.org/abs/2307.03941)**  
  Zhang et al. · *AI and Ethics* · 2023-07 · `📄 peer-reviewed` · 117 citations (S2)  
  [[Paper](https://arxiv.org/abs/2307.03941)]  
  Examines how data-erasure rights under the GDPR challenge LLM-based systems, which store and process information differently from search engine indexes. Discusses technical solutions including differential privacy, machine unlearning, model editing and guardrails.

- **[A Survey of Machine Unlearning](https://arxiv.org/abs/2209.02299)**  
  Nguyen et al. · *ACM TIST* · 2022-09 · `📄 peer-reviewed` · 515 citations (S2)  
  [[Paper](https://arxiv.org/abs/2209.02299)]  
  Surveys machine unlearning's concepts, scenarios, methods and applications, motivated by right-to-be-forgotten regulation. Covers formulations, design criteria, removal requests and algorithms, and highlights current trends and new research areas.

### Interpretability

- **[Sparse Autoencoders for Mechanistic Interpretability in NLP: A Critical Survey of Recoverability, Interpretability, and Utility](https://arxiv.org/abs/2610.20139)**  
  Salima Lamsiyah et al. · *Preprint* · 2026-10 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.20139)]  
  Surveys 138 studies on sparse autoencoders in NLP, proposing a task-grounded taxonomy that links dictionary design, feature operations and NLP functions, and assessing evidence on recoverability, interpretability, faithfulness and behavioral utility.

- **[Mechanistic Interpretability of LLM Behavior: A Survey](https://doi.org/10.20944/preprints202610.2446.v1)**  
  Virginia Tech · *Preprints.org* · 2026-10 · `📝 preprint`  
  [[Paper](https://doi.org/10.20944/preprints202610.2446.v1)]  
  Surveys 229 papers across five behavior families (epistemic, linguistic, reasoning, safety, social) and grades mechanistic evidence on five levels, from decodability to generalization.

- **[A Survey on the Linear Representation Hypothesis](https://arxiv.org/abs/2609.22695)**  
  Sewoong Lee et al. · *BlackboxNLP 2026* · 2026-09 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2609.22695)]  
  Analyzes inconsistencies in how the linear representation hypothesis is treated across AI, neuroscience and cognitive science, and proposes a formalization that makes dependencies on model, representation location, feature definition and evaluation dataset explicit, plus open problems.

- **[A Survey on Actionable Interpretability in Large Language Models](https://doi.org/10.24963/ijcai.2026/865)**  
  USC · *IJCAI 2026* · 2026-09 · `📄 peer-reviewed` · 1 citations (S2)  
  [[Paper](https://doi.org/10.24963/ijcai.2026/865)]  
  Reviews attributional and mechanistic interpretability methods by whether they lead to an intervention, and how they support hallucination mitigation, knowledge editing, fairness, safety and efficiency in LLMs and VLMs.

- **[Make Mechanistic Interpretability Auditable: A Call to Develop Guidelines via Continuous Collaborative Reviewing](https://arxiv.org/abs/2606.00033)**  
  Michael Lan et al. · *ACL 2026* · 2026-06 · `📄 peer-reviewed` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2606.00033)]  
  Argues that mechanistic interpretability lacks standardized auditing and calls for continuous collaborative reviewing, expert-verified guidelines and protocols, and source-based systems that track the arguments on which claims depend.

- **[Position: Mechanistic Interpretability Must Disclose Identification Assumptions for Causal Claims](https://arxiv.org/abs/2605.08012)**  
  Zezheng Lin, Fengming Liu · *Preprint* · 2026-05 · `📝 preprint` · 1 citations (S2)  
  [[Paper](https://arxiv.org/abs/2605.08012)]  
  Argues that mechanistic interpretability papers should disclose identification assumptions behind causal claims, based on audits of 10 papers across four methodological strands and then 30 papers, and proposes a disclosure norm.

- **[Attention Sink in Transformers: A Survey on Utilization, Interpretation, and Mitigation](https://arxiv.org/abs/2604.10098)**  
  Zunhai Su et al. · *Preprint* · 2026-04 · `📝 preprint` · 11 citations (S2)  
  [[Paper](https://arxiv.org/abs/2604.10098)]  
  Surveys attention sink in Transformers, where attention concentrates on a few uninformative tokens, organizing research into fundamental utilization, mechanistic interpretation and strategic mitigation.

- **[Locate, Steer, and Improve: A Practical Survey of Actionable Mechanistic Interpretability in Large Language Models](https://arxiv.org/abs/2601.14004)**  
  Hengyuan Zhang et al. · *Computer Science Review* · 2026-01 · `📄 peer-reviewed` · 28 citations (S2)  
  [[Paper](https://arxiv.org/abs/2601.14004)]  
  Surveys mechanistic interpretability as an intervention methodology for LLMs, structured as a pipeline of localizing, steering and improving. Categorizes diagnosis and intervention methods by interpretable object and covers gains in alignment, capability and efficiency.

- **[Towards a Mechanistic Understanding of Large Reasoning Models: A Survey of Training, Inference, and Failures](https://arxiv.org/abs/2601.19928)**  
  Yi Hu et al. · *Preprint* · 2026-01 · `📝 preprint` · 6 citations (S2)  
  [[Paper](https://arxiv.org/abs/2601.19928)]  
  Surveys the mechanistic understanding of large reasoning models, organizing findings into training dynamics, reasoning mechanisms and unintended behaviors, and discusses under-explored challenges including applied interpretability, improved methodologies and a unified theoretical framework.

- **[Mechanistic Interpretability for Understanding Language Abilities in Large Language Models: A Survey](https://doi.org/10.20944/preprints202607.1441.v1)**  
  Xufeng Duan et al. · *Preprint* · 2026 · `📝 preprint` · 1 citations (S2)  
  [[Paper](https://doi.org/10.20944/preprints202607.1441.v1)]  
  Surveys mechanistic interpretability work on language abilities in LLMs, covering probing, neuron-level and circuit-level analysis, and causal interventions used to study linguistic competence.

- **[Mechanistic Interpretability for Large Language Model Alignment: Progress, Challenges, and Future Directions](https://doi.org/10.20944/preprints202602.0128.v1)**  
  Usman Naseem · *Preprint* · 2026 · `📝 preprint`  
  [[Paper](https://doi.org/10.20944/preprints202602.0128.v1)]  
  Reviews mechanistic interpretability for LLM alignment, covering techniques such as circuit discovery, feature visualization, activation steering and causal intervention, along with progress, challenges and future directions.

- **[Interpreting Language Models Through Concept Descriptions: A Survey](https://arxiv.org/abs/2510.01048)**  
  Nils Feldhus, Laura Kopf · *BlackboxNLP 2025* · 2025-10 · `📄 peer-reviewed` · 8 citations (S2)  
  [[Paper](https://arxiv.org/abs/2510.01048)]  
  Surveys methods that use generator models to produce natural-language concept descriptions of neurons, attention heads and SAE features, covering generation methods, automated and human evaluation metrics, and underlying datasets. Identifies a need for more rigorous causal evaluation.

- **[A Review of Developmental Interpretability in Large Language Models](https://arxiv.org/abs/2508.15841)**  
  Ihor Kendiukhov · *Preprint* · 2025-08 · `📝 preprint` · 3 citations (S2)  
  [[Paper](https://arxiv.org/abs/2508.15841)]  
  Reviews developmental interpretability in LLMs, moving from static post-hoc analysis to studying training itself, covering probing, causal tracing and circuit analysis, circuit formation, emergent abilities as phase transitions, parallels with human development, safety implications and open challenges.

- **[Mechanistic Interpretability Needs Philosophy](https://arxiv.org/abs/2506.18852)**  
  Iwan Williams et al. · *Preprint* · 2025-06 · `📝 preprint` · 10 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.18852)]  
  Argues that mechanistic interpretability needs ongoing engagement with philosophy to clarify concepts, refine methods and handle epistemic and ethical complexities, illustrating this with three open problems from the MI literature.

- **[Position: Use Sparse Autoencoders to Discover Unknowns](https://arxiv.org/abs/2506.23845)**  
  Kenny Peng et al. · *ICML 2026* · 2025-06 · `📄 peer-reviewed` · 26 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.23845)]  
  Argues that sparse autoencoders are less effective for acting on known concepts but well suited to discovering unknown ones, a distinction that reconciles negative and positive results, and outlines use cases in interpretability, safety, and social and health sciences.

- **[Towards Transparent AI: A Survey on Explainable Large Language Models](https://arxiv.org/abs/2506.21812)**  
  Avash Palikhe et al. · *Preprint* · 2025-06 · `📝 preprint` · 17 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.21812)]  
  Reviews explainability techniques for LLMs categorized by transformer architecture (encoder-only, decoder-only, and encoder-decoder), then covers their evaluation, practical applications, available resources, open challenges, and future directions.

- **[Position: Mechanistic Interpretability Should Prioritize Feature Consistency in SAEs](https://arxiv.org/abs/2505.20254)**  
  Xiangchen Song et al. · *Preprint* · 2025-05 · `📝 preprint` · 18 citations (S2)  
  [[Paper](https://arxiv.org/abs/2505.20254)]  
  Argues that SAE research should prioritize feature consistency across training runs, proposes the PW-MCC metric to measure it, and reports that TopK SAEs reach high consistency on LLM activations with suitable architectural choices.

- **[LLMs for Explainable AI: A Comprehensive Survey](https://arxiv.org/abs/2504.00125)**  
  Ahsan Bilal, David Ebert, Beiyu Lin · *Preprint* · 2025-04 · `📝 preprint` · 101 citations (S2)  
  [[Paper](https://arxiv.org/abs/2504.00125)]  
  Surveys approaches that use LLMs to turn complex model outputs into understandable narratives, covering evaluation techniques for LLM-generated explanations, challenges and limitations, real-world applications, and future directions.

- **[A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models](https://arxiv.org/abs/2503.05613)**  
  Dong Shu et al. · *Findings of EMNLP 2025* · 2025-03 · `📄 peer-reviewed` · 94 citations (S2)  
  [[Paper](https://arxiv.org/abs/2503.05613)]  
  Surveys sparse autoencoders for interpreting LLMs, covering their architecture, design improvements and training strategies, input-based and output-based feature explanation methods, structural and functional evaluation metrics, and applications to understanding and manipulating model behavior.

- **[A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models](https://arxiv.org/abs/2502.17516)**  
  Zihao Lin et al. · *Preprint* · 2025-02 · `📝 preprint` · 42 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.17516)]  
  Surveys mechanistic interpretability for multimodal foundation models, including contrastive and generative vision-language models and text-to-image models, covering adaptation of LLM interpretability methods and mechanistic differences from unimodal models, organized in a structured taxonomy of methods.

- **[Open Problems in Mechanistic Interpretability](https://arxiv.org/abs/2501.16496)**  
  Lee Sharkey et al. · *Preprint* · 2025-01 · `📝 preprint` · 218 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.16496)]  
  Discusses, as a forward-facing review, the frontier of mechanistic interpretability and its open problems, spanning conceptual and practical improvements to methods, applying them to specific scientific and engineering goals, and socio-technical challenges.

- **[Explainable and Interpretable Multimodal Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2412.02104)**  
  Yunkai Dang et al. · *Preprint* · 2024-12 · `📝 preprint` · 95 citations (S2)  
  [[Paper](https://arxiv.org/abs/2412.02104)]  
  Surveys interpretability and explainability of multimodal LLMs, proposing a framework that categorizes research by data, model, and training and inference, and analyzing token-level to embedding-level representations, architecture analysis and design, and transparency-enhancing strategies.

- **[Mechanistic?](https://arxiv.org/abs/2410.09087)**  
  Naomi Saphra, Sarah Wiegreffe · *BlackboxNLP 2024* · 2024-10 · `📄 peer-reviewed` · 62 citations (S2)  
  [[Paper](https://arxiv.org/abs/2410.09087)]  
  Distinguishes four uses of the term "mechanistic" in interpretability research, from a narrow causal-claim definition to a broad cultural one. Traces the history of the NLP interpretability community and the mechanistic community, arguing the polysemy reflects a divide.

- **[Attention Heads of Large Language Models: A Survey](https://arxiv.org/abs/2409.03752)**  
  Zifan Zheng et al. · *Patterns 2025* · 2024-09 · `📄 peer-reviewed` · 111 citations (S2)  
  [[Paper](https://arxiv.org/abs/2409.03752)]  
  Surveys the roles of attention heads in LLMs through a four-stage framework of Knowledge Recalling, In-Context Identification, Latent Reasoning and Expression Preparation, and divides discovery methods into Modeling-Free and Modeling-Required, alongside evaluation methods and benchmarks.

- **[The Quest for the Right Mediator: Surveying Mechanistic Interpretability Through the Lens of Causal Mediation Analysis](https://arxiv.org/abs/2408.01416)**  
  Aaron Mueller et al. · *Computational Linguistics* · 2024-08 · `📄 peer-reviewed` · 21 citations (S2)  
  [[Paper](https://arxiv.org/abs/2408.01416)]  
  Surveys mechanistic interpretability through causal mediation analysis, taxonomizing the field by the types of causal units (mediators) used and the methods for searching over them. Discusses pros and cons of each and recommends new mediators and standardized evaluations.

- **[The Cognitive Revolution in Interpretability: From Explaining Behavior to Interpreting Representations and Algorithms](https://arxiv.org/abs/2408.05859)**  
  Adam Davies, Ashkan Khakzar · *Preprint* · 2024-08 · `📝 preprint` · 21 citations (S2)  
  [[Paper](https://arxiv.org/abs/2408.05859)]  
  Grounds mechanistic interpretability in cognitive science, arguing for a shift from explaining behavior to interpreting representations, echoing psychology's move beyond behaviorism. Proposes a taxonomy of semantic interpretation (learned representations) and algorithmic interpretation (operations over them).

- **[A Practical Review of Mechanistic Interpretability for Transformer-Based Language Models](https://arxiv.org/abs/2407.02646)**  
  Daking Rai et al. · *Preprint* · 2024-07 · `📝 preprint` · 160 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.02646)]  
  Surveys mechanistic interpretability for transformer-based language models from a task-centric perspective, organizing its taxonomy around research questions. Outlines objects of study, techniques, evaluation methods and key findings for each task, as a roadmap for newcomers.

- **[XAI meets LLMs: A Survey of the Relation between Explainable AI and Large Language Models](https://arxiv.org/abs/2407.15248)**  
  Erik Cambria et al. · *Preprint* · 2024-07 · `📝 preprint` · 58 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.15248)]  
  Surveys the relation between XAI and LLM research, examining two paths, improving performance through XAI and interpreting models, and covering both peer-reviewed and arXiv preprint papers while advocating balanced progress in both fields.

- **[Position: An Inner Interpretability Framework for AI Inspired by Lessons from Cognitive Neuroscience](https://arxiv.org/abs/2406.01352)**  
  Martina G. Vilas et al. · *ICML 2024* · 2024-06 · `📄 peer-reviewed` · 12 citations (S2)  
  [[Paper](https://arxiv.org/abs/2406.01352)]  
  Proposes a conceptual framework for building mechanistic explanations in AI inner interpretability, drawing lessons from cognitive neuroscience, and gives concrete methodological strategies to address recent critiques of the field.

- **[A Primer on the Inner Workings of Transformer-based Language Models](https://arxiv.org/abs/2405.00208)**  
  Javier Ferrando et al. · *Preprint* · 2024-05 · `📝 preprint` · 112 citations (S2)  
  [[Paper](https://arxiv.org/abs/2405.00208)]  
  Introduces techniques for interpreting the inner workings of Transformer-based language models, focusing on decoder-only architectures. Overviews known internal mechanisms these models implement, with connections across popular approaches and active research directions.

- **[Interpretability Needs a New Paradigm](https://arxiv.org/abs/2405.05386)**  
  Madsen et al. · *Preprint* · 2024-05 · `📄 peer-reviewed` · 17 citations (S2)  
  [[Paper](https://arxiv.org/abs/2405.05386)]  
  Argues that interpretability should explore new paradigms while staying vigilant about faithfulness, examining the intrinsic and post-hoc paradigms and presenting three emerging ones: easily measurable faithfulness, optimized faithful explanations, and joint prediction-and-explanation models.

- **[Mechanistic Interpretability for AI Safety -- A Review](https://arxiv.org/abs/2404.14082)**  
  Leonard Bereska, Efstratios Gavves · *TMLR* · 2024-04 · `📄 peer-reviewed` · 579 citations (S2)  
  [[Paper](https://arxiv.org/abs/2404.14082)]  
  Reviews mechanistic interpretability for AI safety, which reverse engineers network computations into human-understandable algorithms and concepts. Covers foundational concepts such as features, methodologies for causally dissecting behavior, benefits and risks, and challenges of scalability and automation.

- **[How to use and interpret activation patching](https://arxiv.org/abs/2404.15255)**  
  Stefan Heimersheim, Neel Nanda · *Preprint* · 2024-04 · `📝 preprint` · 253 citations (S2)  
  [[Paper](https://arxiv.org/abs/2404.15255)]  
  Provides advice and best practices for applying activation patching, covering the different ways to apply it, how to interpret results as evidence about circuits, and the choice of metric and its pitfalls.

- **[Usable XAI: 10 Strategies Towards Exploiting Explainability in the LLM Era](https://arxiv.org/abs/2403.08946)**  
  Xuansheng Wu et al. · *ACM TKDD* · 2024-03 · `📄 peer-reviewed` · 102 citations (S2)  
  [[Paper](https://arxiv.org/abs/2403.08946)]  
  Introduces 10 strategies for using explainability with LLMs, covering how XAI can explain and improve LLM-based systems and how LLMs can improve XAI techniques, with key techniques and associated challenges for each.

- **[An introduction to graphical tensor notation for mechanistic interpretability](https://arxiv.org/abs/2402.01790)**  
  Jordan K. Taylor · *Preprint* · 2024-02 · `📝 preprint` · 11 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.01790)]  
  Introduces graphical tensor notation and applies it first to decompositions such as SVD, CP, Tucker and tensor networks, then to foundational approaches for understanding language models, ending with an induction head circuit example.

- **[Towards Uncovering How Large Language Model Works: An Explainability Perspective](https://arxiv.org/abs/2402.10688)**  
  Haiyan Zhao et al. · *Preprint* · 2024-02 · `📝 preprint` · 34 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.10688)]  
  Reviews how knowledge is composed in LLM parameters via mechanistic interpretability and embedded in representations via probing and representation engineering, then examines training dynamics such as grokking and memorization and applications to editing, pruning, and alignment.

- **[Rethinking Interpretability in the Era of Large Language Models](https://arxiv.org/abs/2402.01761)**  
  Chandan Singh et al. · *Preprint* · 2024-02 · `📝 preprint` · 161 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.01761)]  
  Argues that LLMs offer an opportunity to redefine interpretability with broader scope, including auditing LLMs; reviews evaluation of both interpreting LLMs and using LLMs for explanation, and highlights dataset analysis and interactive explanations as priorities.

- **[From Understanding to Utilization: A Survey on Explainability for Large Language Models](https://arxiv.org/abs/2401.12874)**  
  Haoyan Luo, Lucia Specia · *Preprint* · 2024-01 · `📝 preprint` · 66 citations (S2)  
  [[Paper](https://arxiv.org/abs/2401.12874)]  
  Surveys explainability for pre-trained Transformer LLMs, classifying methods into local and global analyses, then covering uses in model editing, controlled generation, and model enhancement, along with evaluation metrics and datasets.

- **[Explaining AI through mechanistic interpretability](https://doi.org/10.1007/s13194-024-00614-4)**  
  Lena Kästner, Barnaby Crook · *European Journal for Philosophy of Science* · 2024 · `📄 peer-reviewed` · 49 citations (S2)  
  [[Paper](https://doi.org/10.1007/s13194-024-00614-4)]  
  Offers a philosophy-of-science account of explanation in mechanistic interpretability, treating the field's results as explanations of how AI systems work.

- **[Concept-based Explainable Artificial Intelligence: A Survey](https://arxiv.org/abs/2312.12936)**  
  Eleonora Poeta et al. · *ACM Computing Surveys* · 2023-12 · `📄 peer-reviewed` · 161 citations (S2)  
  [[Paper](https://arxiv.org/abs/2312.12936)]  
  Reviews concept-based explainable AI methods, defining concepts and explanation types, presenting a taxonomy of nine categories with guidelines for choosing one, and reporting common evaluation strategies including metrics, human evaluations, and datasets.

- **[Explainability of Vision Transformers: A Comprehensive Review and New Perspectives](https://arxiv.org/abs/2311.06786)**  
  Rojina Kashefi et al. · *Multimedia Tools and Applications* · 2023-11 · `📄 peer-reviewed` · 34 citations (S2)  
  [[Paper](https://arxiv.org/abs/2311.06786)]  
  Reviews explainability methods for vision transformers, organizing them in a taxonomy by motivations, structures, and application scenarios, and covering evaluation criteria, tools and frameworks, unexplored aspects, and future research directions.

- **[Explainability for Large Language Models: A Survey](https://arxiv.org/abs/2309.01029)**  
  Haiyan Zhao et al. · *ACM TIST 2024* · 2023-09 · `📄 peer-reviewed` · 994 citations (S2)  
  [[Paper](https://arxiv.org/abs/2309.01029)]  
  Introduces a taxonomy of explainability techniques for Transformer-based language models, split by fine-tuning and prompting paradigms, with local and global explanations in each, plus evaluation metrics, uses for debugging, and open challenges.

- **[Interpretability in Activation Space Analysis of Transformers: A Focused Survey](https://arxiv.org/abs/2302.09304)**  
  Soniya Vijayakumar · *CEUR-WS CIKM 2022 Workshops* · 2023-02 · `📄 peer-reviewed` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2302.09304)]  
  Reviews interpretability methods that examine the activation space formed by neuron activations in transformer feed-forward layers, discussing each work in detail and pointing to future research directions given limited existing research.

- **[Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability](https://arxiv.org/abs/2301.04709)**  
  Atticus Geiger et al. · *JMLR 2025* · 2023-01 · `📄 peer-reviewed` · 245 citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.04709)]  
  Presents causal abstraction as a theoretical foundation for mechanistic interpretability, generalizing it to arbitrary mechanism transformation and formalizing concepts such as polysemantic neurons and the linear representation hypothesis. Unifies methods including activation patching, circuit analysis, sparse autoencoders and steering.

- **[Towards Faithful Model Explanation in NLP: A Survey](https://arxiv.org/abs/2209.11326)**  
  Qing Lyu, Marianna Apidianaki, Chris Callison-Burch · *Computational Linguistics 2024* · 2022-09 · `📄 peer-reviewed` · 268 citations (S2)  
  [[Paper](https://arxiv.org/abs/2209.11326)]  
  Reviews over 110 NLP model explanation methods through the lens of faithfulness, covering its definition and evaluation, and groups approaches into five categories: similarity-based, model-internal structure analysis, backpropagation-based, counterfactual intervention, and self-explanatory models.

- **[Toward Transparent AI: A Survey on Interpreting the Inner Structures of Deep Neural Networks](https://arxiv.org/abs/2207.13243)**  
  Tilman Räuker et al. · *IEEE SaTML 2023* · 2022-07 · `📄 peer-reviewed` · 206 citations (S2)  
  [[Paper](https://arxiv.org/abs/2207.13243)]  
  Reviews over 300 works on inner interpretability of deep neural networks. Organizes methods by which network part they explain (weights, neurons, subnetworks or latent representations) and whether they are intrinsic or post hoc, and links interpretability to adjacent fields.

- **[Interpreting Deep Learning Models in Natural Language Processing: A Review](https://arxiv.org/abs/2110.10470)**  
  Xiaofei Sun et al. · *Preprint* · 2021-10 · `📝 preprint` · 55 citations (S2)  
  [[Paper](https://arxiv.org/abs/2110.10470)]  
  Reviews interpretation methods for neural NLP models, organized into training-based, test-based, and hybrid approaches, with sub-categories such as influence-function, KNN-based, attention-based, saliency-based, and perturbation-based methods, and points out deficiencies and future directions.

- **[Neuron-level Interpretation of Deep NLP Models: A Survey](https://arxiv.org/abs/2108.13138)**  
  Hassan Sajjad, Nadir Durrani, Fahim Dalvi · *TACL 2022* · 2021-08 · `📄 peer-reviewed` · 111 citations (S2)  
  [[Paper](https://arxiv.org/abs/2108.13138)]  
  Surveys neuron-level analysis of deep NLP models, covering methods to discover and understand neurons, evaluation methods, major findings including cross-architecture comparisons, applications such as controlling models and domain adaptation, and open issues.

- **[Post-hoc Interpretability for Neural NLP: A Survey](https://arxiv.org/abs/2108.04840)**  
  Andreas Madsen, Siva Reddy, Sarath Chandar · *ACM Computing Surveys 55:155, 2022* · 2021-08 · `📄 peer-reviewed` · 336 citations (S2)  
  [[Paper](https://arxiv.org/abs/2108.04840)]  
  Categorizes recent post-hoc interpretability methods for neural NLP by how they communicate explanations to humans, discusses each method in depth, and examines how the explanations are validated.

- **[Probing Classifiers: Promises, Shortcomings, and Advances](https://arxiv.org/abs/2102.12452)**  
  Yonatan Belinkov · *Computational Linguistics 2022* · 2021-02 · `📄 peer-reviewed` · 1.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/2102.12452)]  
  Reviews the probing classifiers framework, in which a classifier predicts linguistic properties from model representations, and critically examines its promises, methodological shortcomings and advances.

- **[A Survey on Neural Network Interpretability](https://arxiv.org/abs/2012.14261)**  
  Yu Zhang et al. · *IEEE TETCI 5:726–742* · 2020-12 · `📄 peer-reviewed` · 976 citations (S2)  
  [[Paper](https://arxiv.org/abs/2012.14261)]  
  Reviews neural network interpretability research, clarifying definitions and proposing a three-dimensional taxonomy by engagement type (passive versus active), explanation type, and local-to-global focus, then summarizes evaluation methods and research directions.

- **[Explainable Deep Learning: A Field Guide for the Uninitiated](https://arxiv.org/abs/2004.14545)**  
  Gabrielle Ras et al. · *JAIR* · 2020-04 · `📄 peer-reviewed` · 618 citations (S2)  
  [[Paper](https://arxiv.org/abs/2004.14545)]  
  Offers a field guide for newcomers to explainable deep learning, introducing three dimensions that define foundational methods, discussing evaluation of explanations, relating explainability to adjacent research areas, and covering user-oriented explanation design and future directions.

- **[A Primer in BERTology: What we know about how BERT works](https://arxiv.org/abs/2002.12327)**  
  Anna Rogers, Olga Kovaleva, Anna Rumshisky · *TACL* · 2020-02 · `📄 peer-reviewed` · 2.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2002.12327)]  
  Surveys over 150 studies of BERT, covering what information the model learns and how it is represented, modifications to training objectives and architecture, overparameterization, and compression approaches, before outlining future research directions.

- **[On Interpretability of Artificial Neural Networks: A Survey](https://arxiv.org/abs/2001.02522)**  
  Fenglei Fan et al. · *IEEE TRPMS* · 2020-01 · `📄 peer-reviewed` · 437 citations (S2)  
  [[Paper](https://arxiv.org/abs/2001.02522)]  
  Reviews studies on understanding the mechanisms of neural networks under a comprehensive taxonomy, describes applications of interpretability especially in medicine, and discusses future directions such as links to fuzzy logic and brain science.

- **[Zoom In: An Introduction to Circuits](https://doi.org/10.23915/distill.00024.001)**  
  Chris Olah et al. · *Distill* · 2020 · `📄 peer-reviewed` · 853 citations (S2)  
  [[Paper](https://doi.org/10.23915/distill.00024.001)]  
  Lays out a foundational agenda for the circuits research programme, framing neural network understanding around features, circuits and universality.

- **[Analysis Methods in Neural Language Processing: A Survey](https://arxiv.org/abs/1812.08951)**  
  Yonatan Belinkov, James Glass · *TACL 2019* · 2018-12 · `📄 peer-reviewed` · 692 citations (S2)  
  [[Paper](https://arxiv.org/abs/1812.08951)]  
  Surveys analysis methods for neural language processing models, categorizing them by prominent research trends, and highlights existing limitations and potential directions for future work.

- **[Explaining Explanations: An Overview of Interpretability of Machine Learning](https://arxiv.org/abs/1806.00069)**  
  Leilani H. Gilpin et al. · *IEEE DSAA 2018* · 2018-06 · `📄 peer-reviewed` · 2.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/1806.00069)]  
  Defines explainability and uses that definition to classify existing interpretability literature, discusses why current explanatory methods for deep neural networks are insufficient, and suggests future research directions for explanatory AI.

- **[Visual Interpretability for Deep Learning: a Survey](https://arxiv.org/abs/1802.00614)**  
  Quanshi Zhang, Song-Chun Zhu · *Frontiers of IT & EE* · 2018-02 · `📄 peer-reviewed` · 939 citations (S2)  
  [[Paper](https://arxiv.org/abs/1802.00614)]  
  Reviews studies on understanding CNN representations and learning interpretable, disentangled middle-layer representations, covering visualization, diagnosis of pre-trained CNNs, disentanglement, middle-to-end learning, and prospective trends in explainable AI.

- **[A Survey Of Methods For Explaining Black Box Models](https://arxiv.org/abs/1802.01933)**  
  Riccardo Guidotti et al. · *ACM Computing Surveys* · 2018-02 · `📄 peer-reviewed` · 5.6k citations (S2)  
  [[Paper](https://arxiv.org/abs/1802.01933)]  
  Classifies the main problems addressed in black-box explanation literature by the notion of explanation and the type of black box system, helping researchers find relevant proposals and placing open research questions in perspective.

- **[Methods for Interpreting and Understanding Deep Neural Networks](https://arxiv.org/abs/1706.07979)**  
  Grégoire Montavon, Wojciech Samek, Klaus-Robert Müller · *Digital Signal Processing* · 2017-06 · `📄 peer-reviewed` · 2.7k citations (S2)  
  [[Paper](https://arxiv.org/abs/1706.07979)]  
  Introduces techniques for interpreting deep neural networks and explaining their predictions as an entry-level tutorial, with theory, practical tricks, recommendations for use on real data, and a discussion of applications.

- **[Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/abs/1702.08608)**  
  Doshi-Velez, Kim · *Preprint* · 2017-02 · `📄 peer-reviewed` · 5.9k citations (S2)  
  [[Paper](https://arxiv.org/abs/1702.08608)]  
  Argues for a more rigorous science of interpretable machine learning by defining interpretability, describing when it is needed, suggesting a taxonomy for rigorous evaluation, and exposing open questions.

- **[The Mythos of Model Interpretability](https://arxiv.org/abs/1606.03490)**  
  Lipton · *CACM/Queue* · 2016-06 · `📄 peer-reviewed` · 4.9k citations (S2)  
  [[Paper](https://arxiv.org/abs/1606.03490)]  
  Examines the diverse and sometimes discordant motivations for interpretability and the model properties and techniques thought to confer it, contrasting transparency with post-hoc explanation and questioning claims that linear models are interpretable while deep networks are not.

### Rule extraction and neural-symbolic integration

- **[Neuro-Symbolic Artificial Intelligence: A Task-Directed Survey in the Black-Box Models Era](https://arxiv.org/abs/2603.03177)**  
  Giovanni Pio Delvecchio, Lorenzo Molfetta, Gianluca Moro · *IJCAI 2025* · 2026-03 · `📄 peer-reviewed` · 9 citations (S2)  
  [[Paper](https://arxiv.org/abs/2603.03177)]  
  Surveys task-specific advances in neuro-symbolic methods, especially in natural language processing and computer vision, examining how symbolic systems can improve explainability and reasoning. Provides reproducibility details and per-paper comments in an accompanying repository.

- **[Neuro-Symbolic AI in 2024: A Systematic Review](https://arxiv.org/abs/2501.05435)**  
  Brandon C. Colelough, William Regli · *LNSAI@IJCAI* · 2025-01 · `📄 peer-reviewed` · 108 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.05435)]  
  Reviews neuro-symbolic AI research from 2020 to 2024 using the PRISMA methodology, analyzing 167 papers selected from 1,428 candidates. Maps coverage across learning, reasoning, knowledge representation, explainability and meta-cognition, and identifies gaps.

- **[Rule-Extraction Methods From Feedforward Neural Networks: A Systematic Literature Review](https://arxiv.org/abs/2312.12878)**  
  Sara El Mekkaoui, Loubna Benabbou, Abdelaziz Berrado · *Preprint* · 2023-12 · `📝 preprint` · 3 citations (S2)  
  [[Paper](https://arxiv.org/abs/2312.12878)]  
  Reviews systematically the rule-extraction methods for feedforward neural networks, covering two decades of approaches mostly suited to shallow networks with recent developments for deep learning, limited to supervised learning and crisp rules.

- **[Neurosymbolic AI and its Taxonomy: a survey](https://arxiv.org/abs/2305.08876)**  
  Wandemberg Gibaut et al. · *Preprint* · 2023-05 · `📝 preprint` · 15 citations (S2)  
  [[Paper](https://arxiv.org/abs/2305.08876)]  
  Surveys recent research on models that combine symbolic processing with neural networks, presented as a route toward AGI beyond scaling data and model size. Classifies and compares the models and their applications.

- **[Towards Data-and Knowledge-Driven Artificial Intelligence: A Survey on Neuro-Symbolic Computing](https://arxiv.org/abs/2210.15889)**  
  Wenguan Wang, Yi Yang, Fei Wu · *IEEE TPAMI* · 2022-10 · `📄 peer-reviewed` · 86 citations (S2)  
  [[Paper](https://arxiv.org/abs/2210.15889)]  
  Provides a systematic overview of neuro-symbolic computing, from its history and background to a categorization of recent approaches by neural-symbolic integration, knowledge representation, knowledge embedding and functionality, with applications, benchmarks on three tasks and open problems.

- **[Neuro-symbolic approaches in artificial intelligence](https://doi.org/10.1093/nsr/nwac035)**  
  Pascal Hitzler et al. · *National Science Review* · 2022 · `📄 peer-reviewed` · 194 citations (S2)  
  [[Paper](https://doi.org/10.1093/nsr/nwac035)]  
  Gives an overview of neuro-symbolic approaches in AI, describing how they combine neural network learning with symbolic methods and representations.

- **[The Third AI Summer: AAAI Robert S. Engelmore Memorial Lecture](https://doi.org/10.1002/aaai.12036)**  
  Henry Kautz · *AI Magazine* · 2022 · `📄 peer-reviewed` · 218 citations (S2)  
  [[Paper](https://doi.org/10.1002/aaai.12036)]  
  Presents a memorial lecture laying out an agenda for AI's third summer, and is the origin of a six-type taxonomy of neural-symbolic system designs.

- **[A review of some techniques for inclusion of domain-knowledge into deep neural networks](https://doi.org/10.1038/s41598-021-04590-0)**  
  Tirtharaj Dash et al. · *Scientific Reports* · 2022 · `📄 peer-reviewed` · 198 citations (S2)  
  [[Paper](https://doi.org/10.1038/s41598-021-04590-0)]  
  Reviews ways of injecting prior domain knowledge into deep networks, grouped by whether the knowledge alters the inputs, the loss, or the model.

- **[A Survey on Neural-symbolic Learning Systems](https://arxiv.org/abs/2111.08164)**  
  Dongran Yu et al. · *Neural Networks 2023* · 2021-11 · `📄 peer-reviewed` · 138 citations (S2)  
  [[Paper](https://arxiv.org/abs/2111.08164)]  
  Surveys neural-symbolic learning systems, which combine neural perception with symbolic cognition, from four perspectives: challenges, methods, applications and future directions.

- **[From Statistical Relational to Neurosymbolic Artificial Intelligence: a Survey](https://arxiv.org/abs/2108.11451)**  
  Giuseppe Marra et al. · *Artificial Intelligence* · 2021-08 · `📄 peer-reviewed` · 155 citations (S2)  
  [[Paper](https://arxiv.org/abs/2108.11451)]  
  Surveys the integration of learning and reasoning in neurosymbolic and statistical relational AI, characterizing systems along seven shared dimensions such as logical inference, syntax, semantics, learning scope, representations and learning tasks.

- **[Neuro-Symbolic Artificial Intelligence: Current Trends](https://arxiv.org/abs/2105.05330)**  
  Md Kamruzzaman Sarker et al. · *AI Communications* · 2021-05 · `📄 peer-reviewed` · 155 citations (S2)  
  [[Paper](https://arxiv.org/abs/2105.05330)]  
  Provides a structured overview of current neuro-symbolic AI trends by categorizing recent publications from key conferences, intended as a starting point for research on the topic.

- **[Neuro-Symbolic Artificial Intelligence: The State of the Art](https://doi.org/10.3233/FAIA342)**  
  Pascal Hitzler, Md Kamruzzaman Sarker (eds.) · *IOS Press FAIA* · 2021 · `📄 peer-reviewed` · 130 citations (S2)  
  [[Paper](https://doi.org/10.3233/FAIA342)]  
  Compiles an edited volume of chapters presenting the state of the art in combining symbolic methods with neural networks.

- **[Neurosymbolic AI: The 3rd Wave](https://arxiv.org/abs/2012.05876)**  
  Artur d'Avila Garcez, Luís C. Lamb · *Artificial Intelligence Review 2023* · 2020-12 · `📄 peer-reviewed` · 714 citations (S2)  
  [[Paper](https://arxiv.org/abs/2012.05876)]  
  Relates early and recent neurosymbolic research that integrates neural learning with symbolic knowledge representation and logical reasoning, drawing on 20 years of work to identify key ingredients and challenges for the next decade.

- **[Extracting Relational Explanations From Deep Neural Networks: A Survey From a Neural-Symbolic Perspective](https://doi.org/10.1109/TNNLS.2019.2944672)**  
  Joe Townsend, Thomas Chaton, João M. Monteiro · *IEEE TNNLS* · 2020 · `📄 peer-reviewed` · 70 citations (S2)  
  [[Paper](https://doi.org/10.1109/TNNLS.2019.2944672)]  
  Surveys work connecting rule extraction with neural-symbolic integration, covering how relational explanations can be obtained from deep neural networks.

- **[Neural-Symbolic Computing: An Effective Methodology for Principled Integration of Machine Learning and Reasoning](https://arxiv.org/abs/1905.06088)**  
  Artur d'Avila Garcez et al. · *FLAP / Journal of Applied Logics* · 2019-05 · `📄 peer-reviewed` · 433 citations (S2)  
  [[Paper](https://arxiv.org/abs/1905.06088)]  
  Surveys recent neural-symbolic computing work as a principled way to integrate machine learning and reasoning, outlining the methodology's main characteristics and its role in building explainable, accountable AI systems.

- **[Informed Machine Learning -- A Taxonomy and Survey of Integrating Knowledge into Learning Systems](https://arxiv.org/abs/1903.12394)**  
  Laura von Rueden et al. · *IEEE TKDE* · 2019-03 · `📄 peer-reviewed` · 957 citations (S2)  
  [[Paper](https://arxiv.org/abs/1903.12394)]  
  Introduces a taxonomy of approaches that integrate prior knowledge into machine learning, classifying them by knowledge source, representation, and integration point in the pipeline. Surveys papers covering representations such as algebraic equations, logic rules and simulation results.

- **[Neural-Symbolic Learning and Reasoning: A Survey and Interpretation](https://arxiv.org/abs/1711.03902)**  
  Tarek R. Besold et al. · *Preprint* · 2017-11 · `📝 preprint` · 519 citations (S2)  
  [[Paper](https://arxiv.org/abs/1711.03902)]  
  Surveys neural-symbolic learning and reasoning through the views of several researchers, in three parts: scope and theoretical foundations, systems and applications, and challenges with directions for future research.

- **[Rule Extraction Algorithm for Deep Neural Networks: A Review](https://arxiv.org/abs/1610.05267)**  
  Tameru Hailesilassie · *IJCSIS 14:371–381* · 2016-10 · `📄 peer-reviewed` · 106 citations (S2)  
  [[Paper](https://arxiv.org/abs/1610.05267)]  
  Reviews rule extraction algorithms for deep neural networks, classifying them as decompositional, pedagogical or eclectic and evaluating them by the network structure each targets, and finds limited study of deep-network extraction.

- **[Rule extraction from neural networks — A comparative study](https://doi.org/10.1109/ICPRIME.2012.6208380)**  
  M. Gethsiyal Augasta, T. Kathirvalavakumar · *PRIME-2012, IEEE* · 2012 · `📄 peer-reviewed` · 55 citations (S2)  
  [[Paper](https://doi.org/10.1109/ICPRIME.2012.6208380)]  
  Compares existing rule-extraction methods for neural networks side by side, contrasting how the approaches differ and perform, without proposing a new method.

- **[Rule extraction from support vector machines: A review](https://doi.org/10.1016/j.neucom.2010.02.016)**  
  Nahla Barakat, Andrew P. Bradley · *Neurocomputing* · 2010 · `📄 peer-reviewed` · 224 citations (S2)  
  [[Paper](https://doi.org/10.1016/j.neucom.2010.02.016)]  
  Reviews rule extraction from support vector machines, a model family adjacent to neural networks, and reuses the ADT taxonomy to categorize the extraction approaches.

- **[Rule Extraction from Support Vector Machines](https://doi.org/10.1007/978-3-540-75390-2)**  
  Joachim Diederich (ed.) · *Studies in Computational Intelligence* · 2008 · `📄 peer-reviewed` · 223 citations (S2)  
  [[Paper](https://doi.org/10.1007/978-3-540-75390-2)]  
  Collects edited chapters on rule extraction from support vector machines, covering methods for deriving comprehensible rules from trained SVM models.

- **[Neural-Symbolic Cognitive Reasoning](https://doi.org/10.1007/978-3-540-73246-4)**  
  Artur S. d'Avila Garcez, Luís C. Lamb, Dov M. Gabbay · *Springer Cognitive Technologies* · 2008 · `📄 peer-reviewed` · 249 citations (S2)  
  [[Paper](https://doi.org/10.1007/978-3-540-73246-4)]  
  Presents a book-length treatment of reasoning in neural-symbolic systems, combining connectionist learning with logic for cognitive reasoning and learning.

- **[Perspectives of Neural-Symbolic Integration](https://doi.org/10.1007/978-3-540-73954-8)**  
  Barbara Hammer, Pascal Hitzler (eds.) · *Studies in Computational Intelligence* · 2007 · `📄 peer-reviewed` · 98 citations (S2)  
  [[Paper](https://doi.org/10.1007/978-3-540-73954-8)]  
  Collects edited chapters on neural-symbolic integration, spanning approaches to combining connectionist learning with symbolic knowledge representation and reasoning.

- **[Rule Extraction from Recurrent Neural Networks: A Taxonomy and Review](https://doi.org/10.1162/0899766053630350)**  
  Henrik Jacobsson · *Neural Computation* · 2005 · `📄 peer-reviewed` · 185 citations (S2)  
  [[Paper](https://doi.org/10.1162/0899766053630350)]  
  Reviews methods for extracting finite-state machines and rules from recurrent neural networks, organizing them within a taxonomy of extraction approaches.

- **[Dimensions of Neural-symbolic Integration — A Structured Survey](https://arxiv.org/abs/cs/0511042)**  
  Sebastian Bader, Pascal Hitzler · *We Will Show Them! Essays in Honour of Dov Gabbay* · 2005 · `📄 peer-reviewed` · 161 citations (S2)  
  [[Paper](https://arxiv.org/abs/cs/0511042)]  
  Surveys neural-symbolic integration, covering how connectionist systems handle symbolic knowledge and the logics involved, and classifies systems by their architectures and abilities along several dimensions.

- **[Neural-Symbolic Learning Systems: Foundations and Applications](https://doi.org/10.1007/978-1-4471-0211-3)**  
  Artur S. d'Avila Garcez, Krysia B. Broda, Dov M. Gabbay · *Springer Perspectives in Neural Computing* · 2002 · `📄 peer-reviewed` · 348 citations (S2)  
  [[Paper](https://doi.org/10.1007/978-1-4471-0211-3)]  
  Introduces the CILP approach of translating logic programs into neural networks, alongside knowledge extraction, as a book-length treatment of neural-symbolic learning foundations and applications.

- **[Neuro-fuzzy rule generation: survey in soft computing framework](https://doi.org/10.1109/72.846746)**  
  Sushmita Mitra, Yoichi Hayashi · *IEEE Transactions on Neural Networks* · 2000 · `📄 peer-reviewed` · 790 citations (S2)  
  [[Paper](https://doi.org/10.1109/72.846746)]  
  Surveys fuzzy-rule extraction and generation from neural and neuro-fuzzy models, treating how rule bases are obtained from such networks within a soft computing framework.

- **[Knowledge-Based Neurocomputing](https://doi.org/10.7551/mitpress/4070.001.0001)**  
  Ian Cloete, Jacek M. Zurada (eds.) · *MIT Press* · 2000 · `📄 peer-reviewed` · 74 citations (S2)  
  [[Paper](https://doi.org/10.7551/mitpress/4070.001.0001)]  
  Compiles an edited volume of chapters on knowledge-based neural computing, addressing how knowledge is combined with neural network models.

- **[Using neural networks for data mining](https://doi.org/10.1016/S0167-739X(97)00022-8)**  
  Mark W. Craven, Jude W. Shavlik · *Future Generation Computer Systems* · 1997 · `📄 peer-reviewed` · 302 citations (S2)  
  [[Paper](https://doi.org/10.1016/S0167-739X(97)00022-8)]  
  Surveys approaches that make trained neural networks comprehensible through rule extraction, focusing on the TREPAN-era methods used in data mining.

- **[Combining Symbolic and Neural Learning](https://doi.org/10.1007/BF00993982)**  
  Jude W. Shavlik · *Machine Learning* · 1994 · `📄 peer-reviewed` · 2 citations (S2)  
  [[Paper](https://doi.org/10.1007/BF00993982)]  
  Surveys approaches that combine symbolic and neural learning, giving an overview of how the two paradigms are integrated.

### Weight-space learning, parameter generation and hypernetworks

- **[Position: Weight Space Should Be a First-Class Generative AI Modality](https://arxiv.org/abs/2605.18632)**  
  Zhangyang Wang, Peihao Wang, Kai Wang · *ICML 2026* · 2026-05 · `📄 peer-reviewed` · 8 citations (S2)  
  [[Paper](https://arxiv.org/abs/2605.18632)]  
  Argues that model checkpoints should be treated as a first-class data modality and that generative modeling in weight space should become a core primitive. Organizes existing methods into a five-stage pipeline, surveys practical applications, and clarifies current limits.

- **[Symmetry in Neural Network Parameter Spaces](https://arxiv.org/abs/2506.13018)**  
  Bo Zhao, Robin Walters, Rose Yu · *TMLR* · 2025-06 · `📄 peer-reviewed` · 39 citations (S2)  
  [[Paper](https://arxiv.org/abs/2506.13018)]  
  Surveys symmetries in neural network parameter spaces, meaning transformations that leave the network function unchanged, and how they shape loss landscapes and learning dynamics. Summarizes the literature, links symmetry to learning theory, and identifies gaps.

- **[Where Do We Stand with Implicit Neural Representations? A Technical and Performance Survey](https://arxiv.org/abs/2411.03688)**  
  Amer Essakine et al. · *TMLR 2025* · 2024-11 · `📄 peer-reviewed` · 72 citations (S2)  
  [[Paper](https://arxiv.org/abs/2411.03688)]  
  Reviews implicit neural representation methods, which model data as continuous functions using multilayer perceptrons, under a taxonomy of activation functions, position encoding, combined strategies and network structure optimisation. Includes an experimental comparison across tasks and discusses limitations.

- **[Model Lakes](https://arxiv.org/abs/2403.02327)**  
  Koyena Pal, David Bau, Renée J. Miller · *EDBT 2025* · 2024-03 · `📄 peer-reviewed` · 8 citations (S2)  
  [[Paper](https://arxiv.org/abs/2403.02327)]  
  Introduces the concept of model lakes, inspired by data lakes, for finding, differentiating and understanding collections of deep learning models. Formalizes tasks including attribution, versioning, search and benchmarking, and discusses research challenges and applicable data management techniques.

- **[Learning from models beyond fine-tuning](https://arxiv.org/abs/2310.08184)**  
  Hongling Zheng et al. · *Nature Machine Intelligence 7:6–17* · 2023-10 · `📄 peer-reviewed` · 121 citations (S2)  
  [[Paper](https://arxiv.org/abs/2310.08184)]  
  Reviews methods that adapt foundation models through the model interface without access to raw training data, grouped into five areas: model tuning, distillation, reuse, meta learning and model editing. Closes with open issues and future directions.

- **[Implicit Neural Representation in Medical Imaging: A Comparative Survey](https://arxiv.org/abs/2307.16142)**  
  Molaei et al. · *ICCVW 2023* · 2023-07 · `📄 peer-reviewed` · 196 citations (S2)  
  [[Paper](https://arxiv.org/abs/2307.16142)]  
  Surveys implicit neural representation models in medical imaging, covering reconstruction, segmentation, registration, novel view synthesis and compression. Discusses advantages, limitations, data-related challenges and future directions, and compiles cited studies with open-source implementations.

- **[A Brief Review of Hypernetworks in Deep Learning](https://arxiv.org/abs/2306.06955)**  
  Vinod Kumar Chauhan et al. · *Artificial Intelligence Review 57, art.* · 2023-06 · `📄 peer-reviewed` · 215 citations (S2)  
  [[Paper](https://arxiv.org/abs/2306.06955)]  
  Reviews hypernetworks, which generate weights for a target network, and categorizes them by five design criteria: inputs, outputs, variability of inputs and outputs, and architecture. Covers applications across deep learning problem settings and open challenges.

- **[Dynamic Neural Networks: A Survey](https://arxiv.org/abs/2102.04906)**  
  Yizeng Han et al. · *Preprint* · 2021-02 · `📝 preprint` · 1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2102.04906)]  
  Reviews dynamic networks that adapt their structure or parameters to each input, divided into instance-wise, spatial-wise and temporal-wise categories. Covers architecture design, decision-making schemes, optimization techniques, applications and open problems.

### Meta-learning, learned optimizers and fast weights

- **[Fast weight programming and linear transformers: from machine learning to neurobiology](https://arxiv.org/abs/2508.08435)**  
  Kazuki Irie, Samuel J. Gershman · *TMLR 2025* · 2025-08 · `📄 peer-reviewed` · 8 citations (S2)  
  [[Paper](https://arxiv.org/abs/2508.08435)]  
  Reviews Fast Weight Programmers, recurrent networks with matrix-form hidden states whose fast weights are programmed by a trained network, covering technical foundations, computational characteristics, links to transformers and state space models, and synaptic plasticity models in the brain.

- **[Efficient Attention Mechanisms for Large Language Models: A Survey](https://arxiv.org/abs/2507.19595)**  
  Yutao Sun et al. · *Patterns 7, per S2* · 2025-07 · `📄 peer-reviewed` · 33 citations (S2)  
  [[Paper](https://arxiv.org/abs/2507.19595)]  
  Surveys efficient attention for large language models, split into linear attention (kernel approximations, recurrent formulations, fast-weight dynamics) and sparse attention (fixed patterns, block-wise routing, clustering), covering algorithms, hardware considerations, and pretrained models using efficient or hybrid local-global attention designs.

- **[Learning to optimize: A tutorial for continuous and mixed-integer optimization](https://arxiv.org/abs/2405.15251)**  
  Xiaohan Chen, Jialin Liu, Wotao Yin · *Science China Mathematics* · 2024-05 · `📄 peer-reviewed` · 23 citations (S2)  
  [[Paper](https://arxiv.org/abs/2405.15251)]  
  Introduces learning-to-optimize techniques that use machine learning to accelerate optimization algorithms, estimate solutions quickly, or reshape the problem itself. Considers prerequisites for successful application and problem structure, as a guide for practitioners and researchers.

- **[Meta-learning approaches for few-shot learning: A survey of recent advances](https://arxiv.org/abs/2303.07502)**  
  Hassan Gharoun et al. · *Preprint* · 2023-03 · `📝 preprint` · 244 citations (S2)  
  [[Paper](https://arxiv.org/abs/2303.07502)]  
  Surveys meta-learning approaches for few-shot learning after a brief introduction, organizing recent methods into metric-based, memory-based and learning-based families. Discusses current challenges and directions for future research.

- **[Annotated History of Modern AI and Deep Learning](https://arxiv.org/abs/2212.11279)**  
  Jürgen Schmidhuber · *Preprint* · 2022-12 · `📝 preprint` · 53 citations (S2)  
  [[Paper](https://arxiv.org/abs/2212.11279)]  
  Presents a timeline of significant events in the history of neural networks, machine learning, deep learning, AI and mathematics, crediting foundational contributors from the chain rule onward. Frames machine learning as credit assignment and supplements an earlier deep learning survey.

- **[Tutorial on amortized optimization](https://arxiv.org/abs/2202.00665)**  
  Brandon Amos · *Foundations and Trends in Machine Learning* · 2022-02 · `📄 peer-reviewed` · 130 citations (S2)  
  [[Paper](https://arxiv.org/abs/2202.00665)]  
  Introduces the foundations of amortized optimization, which uses learning to predict solutions to repeated, similar problems. Overviews applications in variational inference, sparse coding, meta-learning, control, reinforcement learning, convex optimization, optimal transport and deep equilibrium networks.

- **[Learning to Optimize: A Primer and A Benchmark](https://arxiv.org/abs/2103.12828)**  
  Tianlong Chen et al. · *JMLR 23:1–59, 2022* · 2021-03 · `📄 peer-reviewed` · 404 citations (S2)  
  [[Paper](https://arxiv.org/abs/2103.12828)]  
  Presents the first comprehensive survey and benchmark of learning to optimize for continuous optimization, setting up taxonomies and categorizing existing works and directions. Benchmarks many approaches on representative problems and releases the Open-L2O software package.

- **[Meta-learning in natural and artificial intelligence](https://arxiv.org/abs/2011.13464)**  
  Jane X. Wang · *Current Opinion in Behavioral Sciences* · 2020-11 · `📄 peer-reviewed` · 170 citations (S2)  
  [[Paper](https://arxiv.org/abs/2011.13464)]  
  Reviews meta-learning across biological and artificial intelligence, recasting research from cognitive science, psychology and neuroscience within a common framework. Discusses recent points of interaction between AI and neuroscience and new directions arising from this perspective.

- **[A Survey of Deep Meta-Learning](https://arxiv.org/abs/2010.03522)**  
  Mike Huisman, Jan N. van Rijn, Aske Plaat · *Artificial Intelligence Review* · 2020-10 · `📄 peer-reviewed` · 442 citations (S2)  
  [[Paper](https://arxiv.org/abs/2010.03522)]  
  Surveys deep meta-learning after laying a theoretical foundation, categorizing key methods as metric-based, model-based or optimization-based techniques. Identifies open challenges such as evaluation on heterogeneous benchmarks and reducing computational cost.

- **[Meta-Learning in Neural Networks: A Survey](https://arxiv.org/abs/2004.05439)**  
  Timothy M. Hospedales et al. · *IEEE TPAMI* · 2020-04 · `📄 peer-reviewed` · 2.9k citations (S2)  
  [[Paper](https://arxiv.org/abs/2004.05439)]  
  Describes the contemporary meta-learning landscape, defining the field and positioning it relative to transfer learning and hyperparameter optimization. Proposes a new taxonomy of methods, surveys applications such as few-shot and reinforcement learning, and discusses challenges.

- **[Generalizing from a Few Examples: A Survey on Few-Shot Learning](https://arxiv.org/abs/1904.05046)**  
  Wang et al. · *ACM Computing Surveys* · 2019-04 · `📄 peer-reviewed` · 2.2k citations (S2)  
  [[Paper](https://arxiv.org/abs/1904.05046)]  
  Surveys few-shot learning from a formal definition, distinguishing it from related problems and arguing the core issue is unreliable empirical risk. Categorizes methods by how prior knowledge is used: data, model or algorithm, and discusses pros, cons and future directions.

- **[Meta-Learning: A Survey](https://arxiv.org/abs/1810.03548)**  
  Joaquin Vanschoren · *Automated Machine Learning* · 2018-10 · `📄 peer-reviewed` · 851 citations (S2)  
  [[Paper](https://arxiv.org/abs/1810.03548)]  
  Provides an overview of meta-learning, the practice of learning from how machine learning approaches perform across many tasks in order to learn new tasks faster. Covers its use in designing pipelines and architectures and replacing hand-engineered algorithms.

- **[Deep Learning in Neural Networks: An Overview](https://arxiv.org/abs/1404.7828)**  
  Jürgen Schmidhuber · *Neural Networks* · 2014-04 · `📄 peer-reviewed` · 18k citations (S2)  
  [[Paper](https://arxiv.org/abs/1404.7828)]  
  Reviews the history of deep learning, distinguishing shallow from deep learners by the depth of their credit assignment paths. Covers supervised learning including the history of backpropagation, unsupervised learning, reinforcement learning, evolutionary computation, and indirect search for short programs encoding large networks.

- **[A Perspective View and Survey of Meta-Learning](https://doi.org/10.1023/A:1019956318069)**  
  Ricardo Vilalta, Youssef Drissi · *Artificial Intelligence Review* · 2002 · `📄 peer-reviewed` · 1.3k citations (S2)  
  [[Paper](https://doi.org/10.1023/A:1019956318069)]  
  Surveys meta-learning from a classical perspective that frames the field as dynamic bias selection, and presents an early overview of the area.

### Neuroevolution and gradient-free search

- **[Neuroevolution: Harnessing Creativity in AI Agent Design](https://neuroevolutionbook.com)**  
  Sebastian Risi et al. · *MIT Press* · 2025 · `📄 peer-reviewed`  
  [[Paper](https://neuroevolutionbook.com)]  
  Presents a textbook on neuroevolution rather than a survey, including a chapter on indirect encodings spanning developmental, grammatical, and hypernetwork approaches, HyperNEAT, and self-attention viewed as a dynamic indirect encoding.

- **[Bridging Evolutionary Algorithms and Reinforcement Learning: A Comprehensive Survey on Hybrid Algorithms](https://arxiv.org/abs/2401.11963)**  
  Pengyi Li et al. · *IEEE TEVC* · 2024-01 · `📄 peer-reviewed` · 118 citations (S2)  
  [[Paper](https://arxiv.org/abs/2401.11963)]  
  Surveys hybrids of evolutionary algorithms and reinforcement learning in three directions: EA-assisted optimization of RL, RL-assisted optimization of EA, and synergistic optimization, analyzing research branches in each, the problems they address, and open challenges.

- **[Evolutionary Reinforcement Learning: A Survey](https://arxiv.org/abs/2303.04150)**  
  Hui Bai, Ran Cheng, Yaochu Jin · *Intelligent Computing* · 2023-03 · `📄 peer-reviewed` · 117 citations (S2)  
  [[Paper](https://arxiv.org/abs/2303.04150)]  
  Surveys methods integrating evolutionary computation into reinforcement learning, categorized by RL research field: hyperparameter optimization, policy search, exploration, reward shaping, meta-RL, and multi-objective RL, then discusses future directions in efficient methods, benchmarks, and scalable platforms.

- **[Survey on Evolutionary Deep Learning: Principles, Algorithms, Applications and Open Issues](https://arxiv.org/abs/2208.10658)**  
  Nan Li et al. · *ACM Computing Surveys* · 2022-08 · `📄 peer-reviewed` · 145 citations (S2)  
  [[Paper](https://arxiv.org/abs/2208.10658)]  
  Analyzes evolutionary deep learning through an AutoML lens, introducing a taxonomy of what and how to evolve across the pipeline from feature engineering and model generation to deployment, with focus on solution representation and search paradigms.

- **[Lights and Shadows in Evolutionary Deep Learning: Taxonomy, Critical Methodological Analysis, Cases of Study, Learned Lessons, Recommendations and Challenges](https://arxiv.org/abs/2008.03620)**  
  Aritz D. Martinez et al. · *Information Fusion* · 2020-08 · `📄 peer-reviewed` · 33 citations (S2)  
  [[Paper](https://arxiv.org/abs/2008.03620)]  
  Reviews and critically examines bio-inspired optimization combined with deep learning along three axes: a taxonomy with historical perspective, a methodological critique with two case studies and recommendations, and challenges for future research.

- **[A Survey on Evolutionary Neural Architecture Search](https://arxiv.org/abs/2008.10937)**  
  Yuqiao Liu et al. · *IEEE TNNLS* · 2020-08 · `📄 peer-reviewed` · 630 citations (S2)  
  [[Paper](https://arxiv.org/abs/2008.10937)]  
  Reviews over 200 papers on evolutionary computation methods for neural architecture search, organized by core components, discussing their design principles and justifications, and outlining current challenges and future research.

- **[Neuroevolution in Deep Neural Networks: Current Trends and Future Challenges](https://arxiv.org/abs/2006.05415)**  
  Edgar Galván, Peter Mooney · *IEEE Transactions on AI* · 2020-06 · `📄 peer-reviewed` · 183 citations (S2)  
  [[Paper](https://arxiv.org/abs/2006.05415)]  
  Reviews evolutionary algorithms used for architectural configuration and training of deep neural networks, evaluating strengths and limitations, and identifying current issues, challenges, and promising future research directions.

- **[A Primer on Zeroth-Order Optimization in Signal Processing and Machine Learning](https://arxiv.org/abs/2006.06224)**  
  Sijia Liu et al. · *IEEE Signal Processing Magazine* · 2020-06 · `📄 peer-reviewed` · 362 citations (S2)  
  [[Paper](https://arxiv.org/abs/2006.06224)]  
  Reviews zeroth-order optimization, which uses only function evaluations through gradient estimation, descent direction computation, and solution update, covering underlying intuition, optimization principles, convergence analysis advances, and applications such as black-box robustness evaluation, explanation generation, and sensor management.

- **[Evolution strategies for continuous optimization: A survey of the state-of-the-art](https://doi.org/10.1016/j.swevo.2020.100694)**  
  Zhenhua Li et al. · *Swarm and Evolutionary Computation 56:100694* · 2020 · `📄 peer-reviewed` · 89 citations (S2)  
  [[Paper](https://doi.org/10.1016/j.swevo.2020.100694)]  
  Reviews the state of the art in evolution strategies, a family of evolutionary algorithms for optimizing over continuous search spaces, as a survey of methods developed in this area.

- **[Derivative-free optimization methods](https://arxiv.org/abs/1904.11585)**  
  Jeffrey Larson, Matt Menickelly, Stefan M. Wild · *Acta Numerica* · 2019-04 · `📄 peer-reviewed` · 139 citations (S2)  
  [[Paper](https://arxiv.org/abs/1904.11585)]  
  Reviews derivative-free, or zeroth-order, optimization for black-box objectives, categorizing methods by assumed properties of the function and method features: deterministic methods, randomized methods, structured objectives, stochastic oracles, and constraint handling.

- **[Designing neural networks through neuroevolution](https://doi.org/10.1038/s42256-018-0006-z)**  
  Kenneth O. Stanley et al. · *Nature Machine Intelligence 1:24–35* · 2019 · `📄 peer-reviewed` · 597 citations (CR)  
  [[Paper](https://doi.org/10.1038/s42256-018-0006-z)]  
  Surveys neuroevolution at deep-learning scale, covering evolution strategies and genetic algorithms for weights, HyperNEAT and CPPN encodings, novelty search, and open-endedness.

- **[The CMA Evolution Strategy: A Tutorial](https://arxiv.org/abs/1604.00772)**  
  Nikolaus Hansen · *Preprint* · 2016-04 · `📝 preprint` · 1.9k citations (S2)  
  [[Paper](https://arxiv.org/abs/1604.00772)]  
  Introduces CMA-ES, a stochastic method for real-parameter optimization of non-linear, non-convex functions, motivating and deriving the algorithm from intuitive concepts and from requirements of continuous-domain search.

- **[Neuroevolution in Games: State of the Art and Open Challenges](https://arxiv.org/abs/1410.7326)**  
  Sebastian Risi, Julian Togelius · *IEEE TCIAIG* · 2014-10 · `📄 peer-reviewed` · 152 citations (S2)  
  [[Paper](https://arxiv.org/abs/1410.7326)]  
  Surveys neuroevolution applied to games, analysing work along five axes: the role neuroevolution plays in a game, network types, how networks are evolved, how fitness is determined, and input types, plus open challenges.

- **[Neuroevolution: from architectures to learning](https://doi.org/10.1007/s12065-007-0002-4)**  
  Dario Floreano, Peter Dürr, Claudio Mattiussi · *Evolutionary Intelligence 1:47–62* · 2008 · `📄 peer-reviewed` · 775 citations (S2)  
  [[Paper](https://doi.org/10.1007/s12065-007-0002-4)]  
  Reviews neuroevolution from evolving architectures to evolving learning, contrasting direct and developmental encodings and covering the evolution of plasticity rules.

- **[A Taxonomy for Artificial Embryogeny](https://doi.org/10.1162/106454603322221487)**  
  Kenneth O. Stanley, Risto Miikkulainen · *Artificial Life* · 2003 · `📄 peer-reviewed` · 511 citations (S2)  
  [[Paper](https://doi.org/10.1162/106454603322221487)]  
  Organizes indirect and developmental encodings into a taxonomy with five dimensions, providing a framework for classifying and comparing approaches that grow solutions rather than specifying them directly.

- **[Evolution strategies – A comprehensive introduction](https://doi.org/10.1023/A:1015059928466)**  
  Hans-Georg Beyer, Hans-Paul Schwefel · *Natural Computing* · 2002 · `📄 peer-reviewed` · 2.9k citations (S2)  
  [[Paper](https://doi.org/10.1023/A:1015059928466)]  
  Introduces evolution strategies, providing a comprehensive introductory overview of this family of evolutionary optimization algorithms and serving as a general entry point to the topic.

- **[Combinations of genetic algorithms and neural networks: a survey of the state of the art](https://doi.org/10.1109/COGANN.1992.273950)**  
  J. David Schaffer, L. Darrell Whitley, Larry J. Eshelman · *COGANN-92 workshop* · 1992 · `📄 peer-reviewed` · 647 citations (S2)  
  [[Paper](https://doi.org/10.1109/COGANN.1992.273950)]  
  Reviews early work in which genetic algorithms set neural network weights, architectures, and learning parameters, giving a state-of-the-art overview of the combination.

### Pruning and compression

- **[A Survey of Low-bit Large Language Models: Basics, Systems, and Algorithms](https://arxiv.org/abs/2409.16694)**  
  Ruihao Gong et al. · *Preprint* · 2024-09 · `📝 preprint` · 50 citations (S2)  
  [[Paper](https://arxiv.org/abs/2409.16694)]  
  Surveys low-bit quantization for large language models from basic, system and algorithm perspectives: data formats and concepts, frameworks across hardware platforms, and techniques and toolkits for low-bit training and inference.

- **[A Survey on Efficient Inference for Large Language Models](https://arxiv.org/abs/2404.14294)**  
  Zixuan Zhou et al. · *Preprint* · 2024-04 · `📝 preprint` · 280 citations (S2)  
  [[Paper](https://arxiv.org/abs/2404.14294)]  
  Surveys efficient LLM inference, analyzing causes of inefficiency such as model size, quadratic attention and autoregressive decoding, and organizing the literature into data-level, model-level and system-level optimization, with comparative experiments on representative methods.

- **[A Survey of Lottery Ticket Hypothesis](https://arxiv.org/abs/2403.04861)**  
  Bohan Liu et al. · *Preprint* · 2024-03 · `📝 preprint` · 33 citations (S2)  
  [[Paper](https://arxiv.org/abs/2403.04861)]  
  Examines research on the Lottery Ticket Hypothesis, the claim that dense networks contain sparse winning subnetworks, from several perspectives, discusses issues in existing work such as efficiency and scalability, and lists directions for further exploration.

- **[Model Compression and Efficient Inference for Large Language Models: A Survey](https://arxiv.org/abs/2402.09748)**  
  Wenxiao Wang et al. · *Preprint* · 2024-02 · `📝 preprint` · 113 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.09748)]  
  Investigates compression and efficient inference for large language models from an algorithmic view, categorizing methods into quantization, pruning, distillation, compact architecture design and dynamic networks, distinguishing medium from large models, and introducing inference frameworks.

- **[A Survey on Transformer Compression](https://arxiv.org/abs/2402.05964)**  
  Yehui Tang et al. · *Preprint* · 2024-02 · `📝 preprint` · 93 citations (S2)  
  [[Paper](https://arxiv.org/abs/2402.05964)]  
  Reviews compression methods for Transformer-based language and vision models, categorized into pruning, quantization, knowledge distillation and efficient architecture design such as Mamba, RetNet and RWKV, and examines relations among the methods.

- **[A Comprehensive Survey of Compression Algorithms for Language Models](https://arxiv.org/abs/2401.15347)**  
  Seungcheol Park et al. · *ACM Computing Surveys* · 2024-01 · `📄 peer-reviewed` · 25 citations (S2)  
  [[Paper](https://arxiv.org/abs/2401.15347)]  
  Surveys language-model compression algorithms spanning pruning, quantization, knowledge distillation, low-rank approximation, parameter sharing and efficient architecture design, summarizing overall trends, analyzing representative algorithms in depth, and proposing future research topics.

- **[Efficient Large Language Models: A Survey](https://arxiv.org/abs/2312.03863)**  
  Zhongwei Wan et al. · *Preprint* · 2023-12 · `📝 preprint` · 276 citations (S2)  
  [[Paper](https://arxiv.org/abs/2312.03863)]  
  Reviews efficient large language model research through a taxonomy of three categories: model-centric, data-centric and framework-centric approaches. Links to a maintained repository that organizes the featured papers.

- **[A Survey on Deep Neural Network Pruning-Taxonomy, Comparison, Analysis, and Recommendations](https://arxiv.org/abs/2308.06767)**  
  Hongrong Cheng, Miao Zhang, Javen Qinfeng Shi · *IEEE TPAMI* · 2023-08 · `📄 peer-reviewed` · 626 citations (S2)  
  [[Paper](https://arxiv.org/abs/2308.06767)]  
  Reviews pruning in a four-part taxonomy: universal or specific speedup, when to prune, how to prune, and fusion with other compression; compares eight pairs of contrast settings and covers LLM and multimodal model pruning.

- **[A Survey on Model Compression for Large Language Models](https://arxiv.org/abs/2308.07633)**  
  Xunyu Zhu et al. · *TACL* · 2023-08 · `📄 peer-reviewed` · 554 citations (S2)  
  [[Paper](https://arxiv.org/abs/2308.07633)]  
  Surveys model compression techniques for large language models, covering quantization, pruning and knowledge distillation, along with benchmarking strategies and evaluation metrics for assessing compressed models.

- **[Structured Pruning for Deep Convolutional Neural Networks: A survey](https://arxiv.org/abs/2303.00566)**  
  Yang He, Lingao Xiao · *IEEE TPAMI* · 2023-03 · `📄 peer-reviewed` · 447 citations (S2)  
  [[Paper](https://arxiv.org/abs/2303.00566)]  
  Surveys structured pruning of deep convolutional networks, comparing techniques by filter ranking, regularization, dynamic execution, neural architecture search, the lottery ticket hypothesis, and applications, while contrasting them with unstructured pruning and outlining research opportunities.

- **[A Survey on Model Compression and Acceleration for Pretrained Language Models](https://arxiv.org/abs/2202.07105)**  
  Canwen Xu, Julian McAuley · *AAAI 2023* · 2022-02 · `📄 peer-reviewed` · 104 citations (S2)  
  [[Paper](https://arxiv.org/abs/2202.07105)]  
  Reviews compression and acceleration of Transformer-based pretrained language models, focusing on the inference stage and covering benchmarks, metrics and methodology within the broader context of efficient NLP.

- **[A Survey of Quantization Methods for Efficient Neural Network Inference](https://arxiv.org/abs/2103.13630)**  
  Amir Gholami et al. · *Low-Power Computer Vision* · 2021-03 · `📄 peer-reviewed` · 1.8k citations (S2)  
  [[Paper](https://arxiv.org/abs/2103.13630)]  
  Surveys approaches to quantizing numerical values in deep neural network computations, covering the advantages and disadvantages of current methods and presenting a snapshot of this active research area for efficient inference.

- **[Sparsity in Deep Learning: Pruning and growth for efficient inference and training in neural networks](https://arxiv.org/abs/2102.00554)**  
  Torsten Hoefler et al. · *JMLR 22:1–124* · 2021-02 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2102.00554)]  
  Surveys sparsity in deep learning and provides a tutorial on sparsification for inference and training, distilling more than 300 papers on removing and adding network elements, training strategies, and exploiting sparsity on hardware, plus open problems.

- **[Pruning and Quantization for Deep Neural Network Acceleration: A Survey](https://arxiv.org/abs/2101.09671)**  
  Tailin Liang et al. · *Neurocomputing* · 2021-01 · `📄 peer-reviewed` · 1.1k citations (S2)  
  [[Paper](https://arxiv.org/abs/2101.09671)]  
  Surveys pruning and quantization for accelerating deep networks, separating static from dynamic pruning and comparing element-, channel-, shape-, filter-, layer- and network-wise granularities. Covers quantization to 8-bit and lower, including binary networks, and offers practical guidance.

- **[A Survey on Deep Neural Network Compression: Challenges, Overview, and Solutions](https://arxiv.org/abs/2010.03954)**  
  Rahul Mishra, Hari Prabhat Gupta, Tanima Dutta · *Preprint* · 2020-10 · `📝 preprint` · 112 citations (S2)  
  [[Paper](https://arxiv.org/abs/2010.03954)]  
  Reviews DNN compression literature aimed at reducing storage and computation for resource-constrained IoT devices, dividing approaches into network pruning, sparse representation, bit precision, knowledge distillation and miscellaneous categories, with challenges per category and future directions.

- **[An Overview of Neural Network Compression](https://arxiv.org/abs/2006.03669)**  
  James O'Neill · *Preprint* · 2020-06 · `📝 preprint` · 126 citations (S2)  
  [[Paper](https://arxiv.org/abs/2006.03669)]  
  Reviews older and current compression techniques for deep networks, including pruning, quantization, tensor decomposition, knowledge distillation and their combinations, mostly in the context of recurrent, convolutional and self-attention architectures.

- **[Knowledge Distillation: A Survey](https://arxiv.org/abs/2006.05525)**  
  Jianping Gou et al. · *IJCV* · 2020-06 · `📄 peer-reviewed` · 4.9k citations (S2)  
  [[Paper](https://arxiv.org/abs/2006.05525)]  
  Surveys knowledge distillation, in which a small student model learns from a large teacher, organized by knowledge categories, training schemes, teacher-student architectures, distillation algorithms, performance comparison and applications, plus open challenges and future directions.

- **[What is the State of Neural Network Pruning?](https://arxiv.org/abs/2003.03033)**  
  Davis Blalock et al. · *MLSys 2020* · 2020-03 · `📄 peer-reviewed` · 1.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/2003.03033)]  
  Presents a meta-analysis of pruning literature, aggregating results across 81 papers and controlled pruning of hundreds of models, finding a lack of standardized benchmarks and metrics, and introducing ShrinkBench, an open-source evaluation framework.

- **[Model Compression and Hardware Acceleration for Neural Networks: A Comprehensive Survey](https://doi.org/10.1109/JPROC.2020.2976475)**  
  Lei Deng et al. · *Proceedings of the IEEE* · 2020 · `📄 peer-reviewed` · 1k citations (S2)  
  [[Paper](https://doi.org/10.1109/JPROC.2020.2976475)]  
  Surveys techniques for compressing neural networks and the hardware used to accelerate them, treating algorithmic model compression and hardware acceleration as the two main areas of coverage.

- **[A Survey of Model Compression and Acceleration for Deep Neural Networks](https://arxiv.org/abs/1710.09282)**  
  Yu Cheng et al. · *Preprint* · 2017-10 · `📝 preprint` · 1.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/1710.09282)]  
  Reviews techniques for compacting and accelerating DNN models in four categories: parameter pruning and quantization, low-rank factorization, transferred or compact convolutional filters, and knowledge distillation, analyzing each, with evaluation metrics, datasets, benchmark efforts, and future challenges.

### Backdoors and weight-level attacks

- **[Open Technical Problems in Open-Weight AI Model Risk Management](https://arxiv.org/abs/2608.07514)**  
  Stephen Casper et al. · *TMLR 2026* · 2026-08 · `📄 peer-reviewed` · 21 citations (S2)  
  [[Paper](https://arxiv.org/abs/2608.07514)]  
  Presents 16 open technical challenges for open-weight model safety across training data, training algorithms, evaluations, deployment and ecosystem monitoring, arguing that openness about research and evaluations is key.

- **[Rethinking Reasoning: A Survey on Reasoning-based Backdoors in LLMs](https://arxiv.org/abs/2510.07697)**  
  Man Hu et al. · *Findings of ACL 2026* · 2025-10 · `📄 peer-reviewed` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2510.07697)]  
  Reviews reasoning-based backdoor attacks in LLMs, proposing a taxonomy that groups them into associative, passive and active attacks, and covers defense strategies, current challenges and future research directions.

- **[Backdoor Attacks and Defenses in Computer Vision Domain: A Survey](https://arxiv.org/abs/2509.07504)**  
  Bilal Hussain Abbasi et al. · *Preprint* · 2025-09 · `📝 preprint` · 3 citations (S2)  
  [[Paper](https://arxiv.org/abs/2509.07504)]  
  Reviews computer-vision backdoor attacks and defenses using a multi-dimensional taxonomy by injection stage, trigger type, labeling strategy, representation stage and target task, and discusses where defenses succeed or fail and gaps such as supply-chain and hardware threats.

- **[Architectural Backdoors in Deep Learning: A Survey of Vulnerabilities, Detection, and Defense](https://arxiv.org/abs/2507.12919)**  
  Victoria Childress, Josh Collyer, Jodie Knapp · *Preprint* · 2025-07 · `📝 preprint` · 4 citations (S2)  
  [[Paper](https://arxiv.org/abs/2507.12919)]  
  Consolidates research on architectural backdoors embedded in a model's computational graph, spanning compiler-level manipulations, tainted AutoML pipelines and supply-chain vulnerabilities, and assesses detection and defense strategies such as static graph inspection, dynamic fuzzing and partial formal verification.

- **[A Comprehensive Survey in LLM(-Agent) Full Stack Safety: Data, Training and Deployment](https://arxiv.org/abs/2504.15585)**  
  Kun Wang et al. · *Preprint* · 2025-04 · `📝 preprint` · 145 citations (S2)  
  [[Paper](https://arxiv.org/abs/2504.15585)]  
  Surveys LLM and agent safety across the full lifecycle of data preparation, pre-training, post-training, deployment and commercialization, drawing on over 800 papers to organize security issues holistically.

- **[Data Poisoning in Deep Learning: A Survey](https://arxiv.org/abs/2503.22759)**  
  Pinlong Zhao et al. · *Preprint* · 2025-03 · `📝 preprint` · 38 citations (S2)  
  [[Paper](https://arxiv.org/abs/2503.22759)]  
  Reviews data poisoning attacks in deep learning, categorizing them from multiple perspectives, extending the discussion to poisoning of large language models, and outlining open challenges and research directions.

- **[A Survey on Backdoor Threats in Large Language Models (LLMs): Attacks, Defenses, and Evaluations](https://arxiv.org/abs/2502.05224)**  
  Yihe Zhou et al. · *Transactions on Artificial Intelligence 2025* · 2025-02 · `📄 peer-reviewed` · 41 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.05224)]  
  Surveys backdoor threats to large language models, adapting a general machine-learning attack taxonomy to training-time white-box backdoor attacks, and covers corresponding defense methods as a guideline for future research.

- **[Safety at Scale: A Comprehensive Survey of Large Model and Agent Safety](https://arxiv.org/abs/2502.05206)**  
  Xingjun Ma et al. · *Preprint* · 2025-02 · `📝 preprint` · 82 citations (S2)  
  [[Paper](https://arxiv.org/abs/2502.05206)]  
  Reviews safety research on vision foundation, language, vision-language and diffusion models and model-powered agents, with a taxonomy of threats from adversarial and backdoor attacks to jailbreaks and extraction, plus defenses, benchmarks and open challenges.

- **[On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://arxiv.org/abs/2412.07097)**  
  Xiangyu Qi et al. · *venue unverified* · 2024-12 · `📄 peer-reviewed` · 68 citations (S2)  
  [[Paper](https://arxiv.org/abs/2412.07097)]  
  Argues that evaluating durable safeguards for open-weight LLMs against adversarial fine-tuning is difficult, using case studies to show evaluation pitfalls and urging claims limited to well-defined, rigorously examined threat models.

- **[Harmful Fine-tuning Attacks and Defenses for Large Language Models: A Survey](https://arxiv.org/abs/2409.18169)**  
  Tiansheng Huang et al. · *ACM Computing Surveys 2026* · 2024-09 · `📄 peer-reviewed` · 107 citations (S2)  
  [[Paper](https://arxiv.org/abs/2409.18169)]  
  Reviews harmful fine-tuning attacks and defenses for LLMs, formulating the threat model and organizing the literature by attack setting, defense design and evaluation methodology, with a curated companion paper list.

- **[A Survey of Trojan Attacks and Defenses to Deep Neural Networks](https://arxiv.org/abs/2408.08920)**  
  Lingxin Jin et al. · *Preprint* · 2024-08 · `📝 preprint` · 7 citations (S2)  
  [[Paper](https://arxiv.org/abs/2408.08920)]  
  Surveys Trojan attacks on deep networks and countermeasures, tracing the concept from traditional Trojans to neural network Trojans, comparing attack and defense strategies, and assessing the feasibility of such attacks in real-world scenarios.

- **[A Survey on Failure Analysis and Fault Injection in AI Systems](https://arxiv.org/abs/2407.00125)**  
  Guangba Yu et al. · *ACM TOSEM 2025* · 2024-07 · `📄 peer-reviewed` · 42 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.00125)]  
  Surveys failure analysis and fault injection approaches across six layers of AI systems, analyzing 160 papers and repositories to build a taxonomy of failures and assess what faults injection tools can simulate.

- **[Open Problems in Technical AI Governance](https://arxiv.org/abs/2407.14981)**  
  Anka Reuel et al. · *TMLR 2025* · 2024-07 · `📄 peer-reviewed` · 94 citations (S2)  
  [[Paper](https://arxiv.org/abs/2407.14981)]  
  Introduces technical AI governance and presents a taxonomy and incomplete catalog of its open problems, as a resource for technical researchers and funders seeking to contribute to AI governance.

- **[A Survey of Recent Backdoor Attacks and Defenses in Large Language Models](https://arxiv.org/abs/2406.06852)**  
  Shuai Zhao et al. · *TMLR* · 2024-06 · `📄 peer-reviewed` · 59 citations (S2)  
  [[Paper](https://arxiv.org/abs/2406.06852)]  
  Surveys backdoor attacks and defenses in large language models from a fine-tuning perspective, classifying attacks into full-parameter fine-tuning, parameter-efficient fine-tuning and no fine-tuning, and discussing future directions such as attacks without fine-tuning and more covert algorithms.

- **[Unique Security and Privacy Threats of Large Language Models: A Comprehensive Survey](https://arxiv.org/abs/2406.07973)**  
  Shang Wang et al. · *ACM Computing Surveys 2025* · 2024-06 · `📄 peer-reviewed` · 79 citations (S2)  
  [[Paper](https://arxiv.org/abs/2406.07973)]  
  Surveys privacy and security threats unique to large language models across four scenarios: pre-training, fine-tuning, deployment and LLM-based agents, and analyzes potential countermeasures for each scenario.

- **[Backdoor Attacks and Countermeasures in Natural Language Processing Models: A Comprehensive Security Review](https://arxiv.org/abs/2309.06055)**  
  Pengzhou Cheng et al. · *IEEE TNNLS 2025* · 2023-09 · `📄 peer-reviewed` · 76 citations (S2)  
  [[Paper](https://arxiv.org/abs/2309.06055)]  
  Reviews backdoor attacks and countermeasures for language models, organizing attacks into four categories by attacker capability and affected stage, and countermeasures into sample inspection and model inspection, with benchmark datasets and comparative evaluations.

- **[A Comprehensive Overview of Backdoor Attacks in Large Language Models within Communication Networks](https://arxiv.org/abs/2308.14367)**  
  Haomiao Yang et al. · *IEEE Network 2024* · 2023-08 · `📄 peer-reviewed` · 90 citations (S2)  
  [[Paper](https://arxiv.org/abs/2308.14367)]  
  Surveys backdoor attacks on large language models in communication networks, proposing a taxonomy of input-triggered, prompt-triggered, instruction-triggered and demonstration-triggered attacks, and analyzes benchmark datasets and open challenges.

- **[Attacks in Adversarial Machine Learning: A Systematic Survey from the Life-cycle Perspective](https://arxiv.org/abs/2302.09457)**  
  Baoyuan Wu et al. · *International Journal of Computer Vision 2026* · 2023-02 · `📄 peer-reviewed` · 40 citations (S2)  
  [[Paper](https://arxiv.org/abs/2302.09457)]  
  Reviews adversarial machine learning attacks from a life-cycle perspective, proposing a unified mathematical framework and taxonomy covering backdoor attacks, weight attacks and adversarial attacks, and clarifying connections and differences among these paradigms.

- **[Backdoor Learning for NLP: Recent Advances, Challenges, and Future Research Directions](https://arxiv.org/abs/2302.06801)**  
  Marwan Omar · *Preprint* · 2023-02 · `📝 preprint` · 20 citations (S2)  
  [[Paper](https://arxiv.org/abs/2302.06801)]  
  Surveys backdoor learning for NLP, covering attack techniques, applications, defenses and mitigation methods, plus evaluation metrics, benchmark datasets, threat models and open challenges, with a continually updated companion paper list.

- **[A Survey of Bit-Flip Attacks on Deep Neural Network and Corresponding Defense Methods](https://doi.org/10.3390/electronics12040853)**  
  Qian et al. · *Electronics 12:853* · 2023 · `📄 peer-reviewed` · 49 citations (S2)  
  [[Paper](https://doi.org/10.3390/electronics12040853)]  
  Surveys bit-flip attacks on deep neural networks and corresponding defense methods, covering fault-injection techniques such as RowHammer, clock glitching and laser injection.

- **[A Survey on Backdoor Attack and Defense in Natural Language Processing](https://arxiv.org/abs/2211.11958)**  
  Xuan Sheng et al. · *IEEE QRS 2022* · 2022-11 · `📄 peer-reviewed` · 32 citations (S2)  
  [[Paper](https://arxiv.org/abs/2211.11958)]  
  Reviews backdoor attacks and defenses in natural language processing, where attackers manipulate training to inject triggers, and summarizes benchmark datasets and open issues for building systems that resist such attacks.

- **[A Survey of Neural Trojan Attacks and Defenses in Deep Learning](https://arxiv.org/abs/2202.07183)**  
  Jie Wang, Ghulam Mubashar Hassan, Naveed Akhtar · *Preprint* · 2022-02 · `📝 preprint` · 31 citations (S2)  
  [[Paper](https://arxiv.org/abs/2202.07183)]  
  Reviews techniques for devising Trojan attacks on deep learning and their defenses, organizing recent literature systematically and explaining key concepts with minimal assumed background, including risks from outsourced training or data annotation.

- **[An Overview of Backdoor Attacks Against Deep Neural Networks and Possible Defences](https://arxiv.org/abs/2111.08429)**  
  Wei Guo, Benedetta Tondi, Mauro Barni · *IEEE Open Journal of Signal Processing 2022* · 2021-11 · `📄 peer-reviewed` · 117 citations (S2)  
  [[Paper](https://arxiv.org/abs/2111.08429)]  
  Reviews published work on training-time backdoor attacks against deep networks and their defenses, classifying them by the attacker's control over training and the defender's ability to verify training data integrity and monitor the network.

- **[Exploiting Vulnerabilities in Deep Neural Networks: Adversarial and Fault-Injection Attacks](https://arxiv.org/abs/2105.03251)**  
  Faiq Khalid, Muhammad Abdullah Hanif, Muhammad Shafique · *Preprint* · 2021-05 · `📝 preprint` · 12 citations (S2)  
  [[Paper](https://arxiv.org/abs/2105.03251)]  
  Overviews vulnerabilities of deep neural networks in cyber-physical systems, covering adversarial and fault-injection attacks, challenges in practical implementation, and prospective approaches toward robust, resilient DNN-based systems.

- **[Security of Neural Networks from Hardware Perspective: A Survey and Beyond](https://doi.org/10.1145/3394885.3431639)**  
  Qian Xu, Md Tanvir Arafin, Gang Qu · *ASP-DAC 2021* · 2021 · `📄 peer-reviewed` · 49 citations (S2)  
  [[Paper](https://doi.org/10.1145/3394885.3431639)]  
  Surveys hardware-level security threats to deep neural networks, including fault injection, and discusses directions beyond the surveyed work.

- **[Dataset Security for Machine Learning: Data Poisoning, Backdoor Attacks, and Defenses](https://arxiv.org/abs/2012.10544)**  
  Micah Goldblum et al. · *IEEE TPAMI 2023* · 2020-12 · `📄 peer-reviewed` · 445 citations (S2)  
  [[Paper](https://arxiv.org/abs/2012.10544)]  
  Categorizes dataset vulnerabilities and exploits in machine learning, covering poisoning and backdoor threat models, defenses and open problems, and develops a unified taxonomy of the threat models and the relationships among them.

- **[Artificial Neural Networks and Fault Injection Attacks](https://arxiv.org/abs/2008.07072)**  
  Shahin Tajik, Fatemeh Ganji · *LNCS book chapter 2022* · 2020-08 · `📄 peer-reviewed` · 13 citations (S2)  
  [[Paper](https://arxiv.org/abs/2008.07072)]  
  Examines security assessment of neural network accelerators under fault injection attacks, comparing their assets with those of cryptographic systems to define threat models, and explores fault attacks mounted on such platforms.

- **[Backdoor Learning: A Survey](https://arxiv.org/abs/2007.08745)**  
  Yiming Li et al. · *IEEE TNNLS* · 2020-07 · `📄 peer-reviewed` · 909 citations (S2)  
  [[Paper](https://arxiv.org/abs/2007.08745)]  
  Surveys backdoor attacks and defenses in deep learning, categorizing existing work, offering a unified framework for analyzing poisoning-based attacks, relating backdoors to adversarial attacks and data poisoning, and summarizing benchmark datasets.

- **[Backdoor Attacks and Countermeasures on Deep Learning: A Comprehensive Review](https://arxiv.org/abs/2007.10760)**  
  Yansong Gao et al. · *Preprint* · 2020-07 · `📝 preprint` · 305 citations (S2)  
  [[Paper](https://arxiv.org/abs/2007.10760)]  
  Organizes backdoor attacks into six categories by attacker capability and pipeline stage and defenses into four classes, comparing their strengths and weaknesses and covering beneficial uses such as intellectual property protection, honeypots and data deletion verification.

- **[A Survey on Impact of Transient Faults on BNN Inference Accelerators](https://arxiv.org/abs/2004.05915)**  
  Navid Khoshavi, Connor Broyles, Yu Bi · *Preprint* · 2020-04 · `📝 preprint` · 9 citations (S2)  
  [[Paper](https://arxiv.org/abs/2004.05915)]  
  Examines the impact of soft errors on binarized neural network inference accelerators, using fault injection on image classifiers trained on CIFAR-10 and MNIST to show drastic accuracy drops.

### LLMs as optimizers and self-improving agents

- **[Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills](https://arxiv.org/abs/2608.01851)**  
  Gaytri Jena et al. · *arXiv* · 2026-08 · `📝 preprint` · 1 citations (S2)  
  [[Paper](https://arxiv.org/abs/2608.01851)]  
  Organizes robot learning by whether competence lives in frozen policy weights (VLA models) or in executable skills that agents write and refine as code. It ranks code-as-policy methods by degree of self-improvement across 77 systems and notes that only the code sense of skill improves without gradient updates.

- **[Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104)**  
  Zhe Ren et al. · *Preprint* · 2026-07 · `📝 preprint` · 24 citations (S2)  
  [[Paper](https://arxiv.org/abs/2607.13104)]  
  Frames modern self-improving agents as a foundation model coupled with a scaffold of prompts, memory, tools and control logic, formalizes self-improvement as a self-induced update operator, and organizes prior work by update target and driving signal.

- **[Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663)**  
  Mingguang Chen, Licheng Wang, Bo Qu · *Preprint* · 2026-07 · `📝 preprint` · 49 citations (S2)  
  [[Paper](https://arxiv.org/abs/2607.07663)]  
  Surveys 1,250 arXiv papers from 2024–2026 along two axes: what the system improves and the degree of loop closure, separating bounded self-refinement from open-ended recursive self-improvement and ordering evaluator signals into a verification hierarchy.

- **[Large Language Models as Optimizers: A Survey of Direct vs. Tool-Augmented Approaches and Their Performance Frontiers](https://arxiv.org/abs/2606.15577)**  
  Roko Peran et al. · *MIPRO 2026* · 2026-06 · `📄 peer-reviewed` · 3 citations (S2)  
  [[Paper](https://arxiv.org/abs/2606.15577)]  
  Surveys LLMs used as optimizers across three paradigms: direct optimization via iterative prompting, tool-augmented optimization that orchestrates external solvers, and tool-creating optimization that discovers reusable algorithms. Describes benchmark-based performance frontiers and argues for trade-offs between direct and tool-augmented approaches.

- **[Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies](https://arxiv.org/abs/2606.23075)**  
  Ruixiao Lin et al. · *Preprint* · 2026-06 · `📝 preprint` · 12 citations (S2)  
  [[Paper](https://arxiv.org/abs/2606.23075)]  
  Analyzes security and privacy threats in self-evolving LLM agent systems using a matrix of five functional modules by five lifecycle stages, identifying seven amplification effects and comparing two open-source frameworks in case studies.

- **[Position: Agentic Evolution is the Path to Evolving LLMs](https://arxiv.org/abs/2602.00359)**  
  Minhua Lin et al. · *Preprint* · 2026-02 · `📝 preprint` · 19 citations (S2)  
  [[Paper](https://arxiv.org/abs/2602.00359)]  
  Argues that agentic evolution, in which an autonomous evolver agent drives deployment-time adaptation, is the future of LLM adaptation, introduces the A-Evolve framework, and proposes an evolution-scaling hypothesis tying adaptation capacity to evolution compute.

- **[A Comprehensive Survey on LLM-Guided Evolutionary Search](https://doi.org/10.20944/preprints202610.1122.v1)**  
  Dongbin Zhao et al. · *Preprint* · 2026 · `📝 preprint`  
  [[Paper](https://doi.org/10.20944/preprints202610.1122.v1)]  
  Surveys LLM-guided evolutionary search, exemplified by AlphaEvolve, and presents itself as the first survey dedicated to this research direction.

- **[Recursive Self-Improvement in AI: A Survey](https://doi.org/10.20944/preprints202609.2680.v1)**  
  Hao Wu et al. · *Preprint* · 2026 · `📝 preprint`  
  [[Paper](https://doi.org/10.20944/preprints202609.2680.v1)]  
  Surveys recursive self-improvement in AI, contrasting approaches that automate the design of AI infrastructure with those that repair existing systems.

- **[AI4AI Survey: From Long-Horizon Agents to Recursive Self-Improvement—Definitions, Reliable Horizons, and Open Problems](https://doi.org/10.20944/preprints202608.2108.v1)**  
  Kai Wu et al. · *Preprint* · 2026 · `📝 preprint`  
  [[Paper](https://doi.org/10.20944/preprints202608.2108.v1)]  
  Surveys the progression from long-horizon agents to recursive self-improvement, covering definitions, reliable horizons and open problems, with a section on self-modifying systems and a thesis about a composition gap.

- **[A Survey of AI Scientists](https://arxiv.org/abs/2510.23045)**  
  Guiyao Tie, Pan Zhou, Lichao Sun · *Preprint* · 2025-10 · `📝 preprint` · 10 citations (S2)  
  [[Paper](https://arxiv.org/abs/2510.23045)]  
  Surveys AI scientist systems through a six-stage framework spanning literature review, idea generation, experimental preparation, experimental execution, scientific writing and paper generation, and traces the field's evolution from foundational modules to closed-loop systems and current scalability work.

- **[A Systematic Survey on Large Language Models for Evolutionary Optimization: From Modeling to Solving](https://arxiv.org/abs/2509.08269)**  
  Yisong Zhang et al. · *IEEE Computational Intelligence Magazine 2026* · 2025-09 · `📄 peer-reviewed` · 19 citations (S2)  
  [[Paper](https://arxiv.org/abs/2509.08269)]  
  Reviews large language models for evolutionary optimization through a workflow of optimization modeling and optimization solving, splitting solving into stand-alone optimizers, embedded low-level components, and high-level managers for algorithm selection and generation, plus benchmarks and applications.

- **[Large Language Model-based Data Science Agent: A Survey](https://arxiv.org/abs/2508.02744)**  
  Ke Chen et al. · *TMLR 2026* · 2025-08 · `📄 peer-reviewed` · 30 citations (S2)  
  [[Paper](https://arxiv.org/abs/2508.02744)]  
  Reviews LLM-based agents for data science from two perspectives: agent design principles covering roles, execution, knowledge and reflection, and data science processes such as preprocessing, model development, evaluation and visualization, linked by a dual-perspective framework.

- **[A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407)**  
  Jinyuan Fang et al. · *Preprint* · 2025-08 · `📝 preprint` · 222 citations (S2)  
  [[Paper](https://arxiv.org/abs/2508.07407)]  
  Reviews self-evolving AI agents through a unified feedback-loop framework of system inputs, agent system, environment and optimisers, surveying techniques targeting each component, domain-specific strategies in biomedicine, programming and finance, and evaluation, safety and ethics.

- **[From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery](https://arxiv.org/abs/2508.14111)**  
  Jiaqi Wei et al. · *Preprint* · 2025-08 · `📝 preprint` · 102 citations (S2)  
  [[Paper](https://arxiv.org/abs/2508.14111)]  
  Reviews autonomous scientific discovery across life sciences, chemistry, materials science and physics, unifying process-, autonomy- and mechanism-oriented perspectives in a framework with five core capabilities and a four-stage discovery workflow.

- **[A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046)**  
  Huan-ang Gao et al. · *TMLR 01/2026* · 2025-07 · `📄 peer-reviewed` · 182 citations (S2)  
  [[Paper](https://arxiv.org/abs/2507.21046)]  
  Reviews self-evolving agents along three dimensions: what to evolve across agent components such as models, memory, tools and architecture, when to adapt by stage, and how, plus benchmarks, applications in coding, education and healthcare, and open challenges.

- **[AI4Research: A Survey of Artificial Intelligence for Scientific Research](https://arxiv.org/abs/2507.01903)**  
  Qiguang Chen et al. · *Science China Information Sciences 2026* · 2025-07 · `📄 peer-reviewed` · 66 citations (S2)  
  [[Paper](https://arxiv.org/abs/2507.01903)]  
  Surveys AI for scientific research with a systematic taxonomy of five mainstream tasks, identifies research gaps and future directions on rigor, scalability and societal impact, and compiles applications, data corpora and tools.

- **[Large Language Models and Evolutionary Computation: A Critical Review of Bidirectional Interaction, Automated Algorithm Design, and Co-Adaptive Systems](https://arxiv.org/abs/2505.15741)**  
  Dikshit Chauhan et al. · *Computer Science Review* · 2025-05 · `📄 peer-reviewed` · 10 citations (S2)  
  [[Paper](https://arxiv.org/abs/2505.15741)]  
  Reviews the bidirectional interaction between LLMs and evolutionary computation, covering EC improving LLM systems via prompt optimization and architecture search, LLMs improving EC via metaheuristic and heuristic design, and co-adaptive feedback-loop frameworks.

- **[From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery](https://arxiv.org/abs/2505.13259)**  
  Tianshi Zheng et al. · *EMNLP 2025* · 2025-05 · `📄 peer-reviewed` · 131 citations (S2)  
  [[Paper](https://arxiv.org/abs/2505.13259)]  
  Surveys LLMs in scientific discovery through a three-level taxonomy of Tool, Analyst and Scientist that reflects escalating autonomy across the research lifecycle, and identifies challenges including robotic automation, self-improvement and ethical governance.

- **[Towards Scientific Intelligence: A Survey of LLM-based Scientific Agents](https://arxiv.org/abs/2503.24047)**  
  Shuo Ren et al. · *Preprint* · 2025-03 · `📝 preprint` · 129 citations (S2)  
  [[Paper](https://arxiv.org/abs/2503.24047)]  
  Reviews LLM-based scientific agents, covering their architectures, design, benchmarks, applications and ethical considerations, and how they differ from general-purpose agents in tasks from hypothesis generation to experiment design, data analysis and simulation.

- **[Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions](https://arxiv.org/abs/2503.08979)**  
  Mourad Gridach et al. · *Preprint* · 2025-03 · `📝 preprint` · 129 citations (S2)  
  [[Paper](https://arxiv.org/abs/2503.08979)]  
  Surveys agentic AI for scientific discovery, categorizing existing systems and tools and their progress in chemistry, biology and materials science, and covering evaluation metrics, implementation frameworks, datasets, challenges such as reliability and ethics, and human-AI collaboration directions.

- **[LLM4SR: A Survey on Large Language Models for Scientific Research](https://arxiv.org/abs/2501.04306)**  
  Ziming Luo et al. · *Preprint* · 2025-01 · `📝 preprint` · 110 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.04306)]  
  Surveys the roles of LLMs across four stages of the research cycle: hypothesis discovery, experiment planning and implementation, scientific writing and peer reviewing, covering task-specific methods, evaluation benchmarks, challenges and future directions.

- **[Large Language Models for Constructing and Optimizing Machine Learning Workflows: A Survey](https://arxiv.org/abs/2411.10478)**  
  Yang Gu et al. · *ACM TOSEM 2026* · 2024-11 · `📄 peer-reviewed` · 39 citations (S2)  
  [[Paper](https://arxiv.org/abs/2411.10478)]  
  Reviews how LLMs construct and optimize machine learning workflows, organized around data and feature engineering, model selection and hyperparameter optimization, and workflow evaluation, with discussion of advantages, limitations, open challenges and future directions.

- **[Deep Insights into Automated Optimization with Large Language Models and Evolutionary Algorithms](https://arxiv.org/abs/2410.20848)**  
  He Yu, Jing Liu · *Preprint* · 2024-10 · `📝 preprint` · 24 citations (S2)  
  [[Paper](https://arxiv.org/abs/2410.20848)]  
  Reviews LLM use in optimization, focusing on LLMs as solution generators and algorithm designers, and proposes an LLM-EA paradigm analyzed through individual representation, variation operators and fitness evaluation.

- **[A Systematic Survey on Large Language Models for Algorithm Design](https://arxiv.org/abs/2410.14716)**  
  Fei Liu et al. · *Preprint* · 2024-10 · `📝 preprint` · 141 citations (S2)  
  [[Paper](https://arxiv.org/abs/2410.14716)]  
  Surveys LLMs for algorithm design with a taxonomy of LLM roles as optimizers, predictors, extractors and designers, synthesizing literature across three pipeline phases and applications, and outlining open challenges.

- **[Open-Endedness is Essential for Artificial Superhuman Intelligence](https://arxiv.org/abs/2406.04268)**  
  Edward Hughes et al. · *Preprint* · 2024-06 · `📝 preprint` · 97 citations (S2)  
  [[Paper](https://arxiv.org/abs/2406.04268)]  
  Argues that open-endedness, formally defined through novelty and learnability, is essential for artificial superhuman intelligence, outlines a path via open-ended systems built on foundation models, and examines safety implications.

- **[Exploring the Improvement of Evolutionary Computation via Large Language Models](https://arxiv.org/abs/2405.02876)**  
  Jinyu Cai et al. · *GECCO 2024 Companion* · 2024-05 · `📄 peer-reviewed` · 11 citations (S2)  
  [[Paper](https://arxiv.org/abs/2405.02876)]  
  Offers a forward-looking overview of how LLMs can improve evolutionary computation, focusing on the algorithms themselves, population design and additional enhancements.

- **[When Large Language Model Meets Optimization](https://arxiv.org/abs/2405.10098)**  
  Sen Huang et al. · *Swarm and Evolutionary Computation 2024* · 2024-05 · `📄 peer-reviewed` · 76 citations (S2)  
  [[Paper](https://arxiv.org/abs/2405.10098)]  
  Reviews the combination of LLMs and optimization algorithms, covering how LLMs support modeling and decision-making in optimization and how optimization algorithms refine LLM architectures and output quality.

- **[A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387)**  
  Zhengwei Tao et al. · *Preprint* · 2024-04 · `📝 preprint` · 100 citations (S2)  
  [[Paper](https://arxiv.org/abs/2404.14387)]  
  Surveys self-evolution of LLMs as iterative cycles of experience acquisition, experience refinement, updating and evaluation, categorizes evolution objectives for LLMs and LLM-based agents, and gives a taxonomy and insights for each module.

- **[Evolutionary Computation in the Era of Large Language Model: Survey and Roadmap](https://arxiv.org/abs/2401.10034)**  
  Xingyu Wu et al. · *IEEE TEVC 2025* · 2024-01 · `📄 peer-reviewed` · 254 citations (S2)  
  [[Paper](https://arxiv.org/abs/2401.10034)]  
  Surveys the interplay of evolutionary algorithms and LLMs, categorizing work into LLM-enhanced EA and EA-enhanced LLM, with integrated methods spanning code generation, software engineering and neural architecture search, plus a roadmap.

- **[When Large Language Models Meet Evolutionary Algorithms: Potential Enhancements and Challenges](https://arxiv.org/abs/2401.10510)**  
  Chao Wang et al. · *Research 2025* · 2024-01 · `📄 peer-reviewed` · 48 citations (S2)  
  [[Paper](https://arxiv.org/abs/2401.10510)]  
  Reviews conceptual parallels between LLMs and evolutionary algorithms at a micro level, then analyzes interdisciplinary research at a macro level, focusing on evolutionary fine-tuning and LLM-enhanced evolutionary algorithms.

- **[AutoML in the Age of Large Language Models: Current Challenges, Future Opportunities and Risks](https://arxiv.org/abs/2306.08107)**  
  Alexander Tornede et al. · *TMLR 2024* · 2023-06 · `📄 peer-reviewed` · 53 citations (S2)  
  [[Paper](https://arxiv.org/abs/2306.08107)]  
  Explores the symbiosis of AutoML and LLMs, surveying existing work on enhancing AutoML with LLMs and on using AutoML to improve LLMs, and critically assessing the risks of integrating the two fields.

- **[AI-GAs: AI-generating algorithms, an alternate paradigm for producing general artificial intelligence](https://arxiv.org/abs/1905.10985)**  
  Jeff Clune · *Preprint* · 2019-05 · `📝 preprint` · 163 citations (S2)  
  [[Paper](https://arxiv.org/abs/1905.10985)]  
  Argues that the AI-generating algorithm approach, built on three pillars of meta-learning architectures, meta-learning learning algorithms and generating learning environments, deserves more research investment than the manual approach to general AI, and discusses safety and ethics.

### Verification and policy reuse

- **[Combining Trained Models in Reinforcement Learning](https://arxiv.org/abs/2605.02159)**  
  Ujjwal Patil, Javad Ghofrani · *Preprint* · 2026-05 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2605.02159)]  
  Presents a PRISMA-guided systematic review of pretrained knowledge reuse in deep reinforcement learning, narrowing 589 retrieved records to 15 empirical studies. Analyzes them by source-target similarity, diversity of reused models, and fairness of comparisons against from-scratch baselines.

- **[Neural Network Verification is a Programming Language Challenge](https://arxiv.org/abs/2501.05867)**  
  Lucas C. Cordeiro et al. · *ESOP 2025* · 2025-01 · `📄 peer-reviewed` · 17 citations (S2)  
  [[Paper](https://arxiv.org/abs/2501.05867)]  
  Argues that neural network verification challenges should be formulated as programming language challenges, and suggests possible future solutions drawing on insights from the programming language community.

- **[Model checking deep neural networks: opportunities and challenges](https://doi.org/10.3389/fcomp.2025.1557977)**  
  Sbai · *Frontiers in Computer Science* · 2025 · `📄 peer-reviewed` · 3 citations (S2)  
  [[Paper](https://doi.org/10.3389/fcomp.2025.1557977)]  
  Takes a model-checking perspective on deep neural networks, outlining the opportunities and challenges of applying that approach to them.

- **[First Three Years of the International Verification of Neural Networks Competition (VNN-COMP)](https://arxiv.org/abs/2301.05815)**  
  Christopher Brix et al. · *STTT 25 329–339* · 2023-01 · `📄 peer-reviewed` · 118 citations (S2)  
  [[Paper](https://arxiv.org/abs/2301.05815)]  
  Summarizes and meta-analyzes the first three annual neural network verification competitions, held in 2020, 2021, and 2022, covering processes, rules, results, and observed trends across problem classes such as image classification, neural control, and reinforcement learning.

- **[Adversarial Robustness of Deep Neural Networks: A Survey from a Formal Verification Perspective](https://arxiv.org/abs/2206.12227)**  
  Mark Huasong Meng et al. · *IEEE TDSC 2024* · 2022-06 · `📄 peer-reviewed` · 99 citations (S2)  
  [[Paper](https://arxiv.org/abs/2206.12227)]  
  Surveys 39 works on adversarial robustness verification for neural networks, analyzing how robustness is formulated and which verification techniques are used. Classifies techniques by property specification, problem reduction, and reasoning strategies.

- **[A Survey of Zero-shot Generalisation in Deep Reinforcement Learning](https://arxiv.org/abs/2111.09794)**  
  Robert Kirk et al. · *JAIR 76:201–264* · 2021-11 · `📄 peer-reviewed` · 323 citations (S2)  
  [[Paper](https://arxiv.org/abs/2111.09794)]  
  Surveys zero-shot generalisation in deep reinforcement learning, using a unifying formalism to categorise existing benchmarks and methods. Offers a critical discussion with recommendations, including building benchmarks in underexplored settings such as offline RL and reward-function variation.

- **[Introduction to Neural Network Verification](https://arxiv.org/abs/2109.10317)**  
  Aws Albarghouthi · *Foundations and Trends in Programming Languages 2021* · 2021-09 · `📄 peer-reviewed` · 122 citations (S2)  
  [[Paper](https://arxiv.org/abs/2109.10317)]  
  Introduces foundational ideas from formal verification and their adaptation to reasoning about the safety, security, correctness, and robustness of neural networks and deep learning, in book-length form.

- **[A Review of Formal Methods applied to Machine Learning](https://arxiv.org/abs/2104.02466)**  
  Caterina Urban, Antoine Miné · *Preprint* · 2021-04 · `📝 preprint` · 81 citations (S2)  
  [[Paper](https://arxiv.org/abs/2104.02466)]  
  Reviews formal methods for verifying machine learning systems, first recalling established methods in avionic software. Notes most methods target trained neural networks using SMT, optimization, or abstract interpretation, and also covers support vector machines and decision tree ensembles.

- **[Towards Continual Reinforcement Learning: A Review and Perspectives](https://arxiv.org/abs/2012.13490)**  
  Khimya Khetarpal et al. · *JAIR 2022* · 2020-12 · `📄 peer-reviewed` · 486 citations (S2)  
  [[Paper](https://arxiv.org/abs/2012.13490)]  
  Reviews formulations and approaches to continual reinforcement learning, offering taxonomies of formulations, based on scope and driver of non-stationarity, and of methods. Covers evaluation benchmarks and metrics, and open problems linking the field to neuroscience.

- **[SoK: Certified Robustness for Deep Neural Networks](https://arxiv.org/abs/2009.04131)**  
  Linyi Li, Tao Xie, Bo Li · *IEEE S&P 2023* · 2020-09 · `📄 peer-reviewed` · 171 citations (S2)  
  [[Paper](https://arxiv.org/abs/2009.04131)]  
  Systematizes certifiably robust approaches for deep neural networks, providing a taxonomy of robustness verification and robust training methods and discussing their strengths, limitations, and connections. Includes an open-source unified platform evaluating more than 20 representative approaches.

- **[Transfer Learning in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2009.07888)**  
  Zhuangdi Zhu et al. · *IEEE TPAMI 2023* · 2020-09 · `📄 peer-reviewed` · 960 citations (S2)  
  [[Paper](https://arxiv.org/abs/2009.07888)]  
  Surveys transfer learning approaches in deep reinforcement learning, proposing a framework that categorizes them and analyzes their goals, methodologies, compatible reinforcement learning backbones, and practical applications. Also connects transfer learning to related topics and outlines future challenges.

- **[Algorithms for Verifying Deep Neural Networks](https://arxiv.org/abs/1903.06758)**  
  Changliu Liu et al. · *Foundations and Trends in Optimization 2021* · 2019-03 · `📄 peer-reviewed` · 502 citations (S2)  
  [[Paper](https://arxiv.org/abs/1903.06758)]  
  Surveys methods for soundly verifying input-output properties of deep neural networks, drawing on reachability analysis, optimization, and search. Discusses connections between algorithms and provides pedagogical implementations compared on benchmark problems.

- **[A Survey of Safety and Trustworthiness of Deep Neural Networks: Verification, Testing, Adversarial Attack and Defence, and Interpretability](https://arxiv.org/abs/1812.08342)**  
  Xiaowei Huang et al. · *Computer Science Review 2020* · 2018-12 · `📄 peer-reviewed` · 456 citations (CR)  
  [[Paper](https://arxiv.org/abs/1812.08342)]  
  Reviews research on making deep neural networks safe and trustworthy, organized around four aspects: verification, testing, adversarial attack and defence, and interpretability. Covers 202 papers, most published after 2017.

- **[Towards Verified Artificial Intelligence](https://arxiv.org/abs/1606.08514)**  
  Sanjit A. Seshia, Dorsa Sadigh, S. Shankar Sastry · *Preprint* · 2016-06 · `📝 preprint` · 220 citations (S2)  
  [[Paper](https://arxiv.org/abs/1606.08514)]  
  Considers verified AI, meaning systems with provable correctness assurances, from a formal methods perspective. Describes five challenges for achieving it and five corresponding principles for addressing them.

- **[Transfer Learning for Reinforcement Learning Domains: A Survey](https://www.jmlr.org/papers/v10/taylor09a.html)**  
  Matthew E. Taylor, Peter Stone · *JMLR 10:1633–1685* · 2009 · `📄 peer-reviewed` · 2.2k citations (S2)  
  [[Paper](https://www.jmlr.org/papers/v10/taylor09a.html)]  
  Surveys the literature on transfer learning in classical reinforcement learning domains, giving an overview of how the topic has been studied.

## Legend

`📄 peer-reviewed` · `📝 preprint` · `💻 code / results` · `💬 post only`

Entries are newest first within each section, except historical sections, which read oldest first. Summaries report the source's own numbers and settings. Evidence labels say what kind of source backs an entry, not whether its claims hold. Citation counts, where shown, are from Semantic Scholar (S2), OpenAlex (OA) or Crossref (CR) at the time the entry was added; the sources are not comparable, so read them as orders of magnitude.

## How This List Is Maintained

An automated sweep (daily) checks arXiv, GitHub and the Hugging Face Hub for new work. Entries need to do weight-space programming or be direct groundwork for it. On-topic papers are listed whatever their traction; repositories are listed once they show traction or come from an organization, and young ones are kept on a watch list and re-checked. Categories grow as the field does: a new section opens when work no longer fits the existing ones. Corrections are welcome as issues or pull requests.

## Related Lists

- [Awesome Weight Space Learning](https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning): learning on and generating weights.
- [Awesome Weight-Space Learning (ege-erdogan)](https://github.com/ege-erdogan/awesome-weight-space-learning)
- [Knowledge Editing Papers](https://github.com/zjunlp/KnowledgeEditingPapers): editing facts in LLMs.
- [Awesome LLM Interpretability](https://github.com/JShollaj/awesome-llm-interpretability)
- [Awesome VLA & WAM](https://github.com/DravenALG/awesome-vla-wam): robot foundation models.
- [awesome-weight-space-programming (brighterr)](https://github.com/brighterr/awesome-weight-space-programming): another list on the same topic.

## Contributing

Contributions are welcome. To add a work, open a pull request that adds one object to [`data/entries.json`](data/entries.json) in the same style as the existing entries, then run `python3 scripts/build.py`. Each pull request is reviewed, and it is merged once its relevance is confirmed. **If you are an author of the work, say so** in the pull request and include the details: affiliation, status (preprint, under review or accepted, and where), links to code and data, and the headline result with its setting. See [CONTRIBUTING.md](CONTRIBUTING.md) for the fields and inclusion rules.

## Citation

```bibtex
@misc{awesome-weight-space-programming,
  author       = {Pakdamansavoji, Sajjad},
  title        = {Awesome Weight-Space Programming},
  year         = {2026},
  howpublished = {\url{https://github.com/SajjadPSavoji/awesome-weight-space-programming}}
}
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=SajjadPSavoji/awesome-weight-space-programming&type=Date)](https://star-history.com/#SajjadPSavoji/awesome-weight-space-programming&Date)
