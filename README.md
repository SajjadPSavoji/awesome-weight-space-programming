<div align="center">

# Awesome Weight-Space Programming [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

**Language models that read, edit and write the weights of other neural networks directly, without gradient descent.**

[![Last commit](https://img.shields.io/github/last-commit/SajjadPSavoji/awesome-weight-space-programming?color=green)](https://github.com/SajjadPSavoji/awesome-weight-space-programming/commits/main)
![Entries](https://img.shields.io/badge/entries-232-blue)
![Updated](https://img.shields.io/badge/updated-daily-orange)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

</div>

*Weight-space programming* was named in the MIT CSAIL report [Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) (2026-11-02). A general LLM is given another network's weights, sometimes with code and a budget of forward passes, and changes the numbers to explain, repair or build behavior. This list tracks the papers, code, benchmarks and critiques that follow, grouped by the kind of network being programmed. The [Foundations](#-foundations-weight-programming-before-wsp) section traces the eighty years of earlier work, from McCulloch and Pitts (1943) to 2025, that read, edited or wrote weights under other names. It is rebuilt from [`data/entries.json`](data/entries.json).

## 🔥 Recently Added

- **2026-11-06** · [IyadhKhalfallah/weight-space-programming](https://github.com/IyadhKhalfallah/weight-space-programming) (Tools, Harnesses and Agent Skills)
- **2026-11-06** · [allthingssecurity/weight_space_programming](https://github.com/allthingssecurity/weight_space_programming) (Writing networks from scratch)
- **2026-11-06** · [fderrigo/weight-space-programming-experiments](https://github.com/fderrigo/weight-space-programming-experiments) (Repairing behavior)
- **2026-11-06** · [sachgaur/WSP](https://github.com/sachgaur/WSP) (Other Domains)
- **2026-11-06** · [Can an LLM Actually Reason and Program about Neural Network's Weights or is it just memorization on steroids? Exploring "Weight-Space Programming"](https://arxiv.org/abs/2611.08070) (Analyses and Critiques)
- **2026-11-06** · [Consistency Is Not Understanding: Orbit Audits for Neural Field Weight Readers](https://arxiv.org/abs/2611.05798) (Benchmarks and Evaluations)
- **2026-11-05** · [Weight-Space Programming (wsp-kit)](https://github.com/AuremHQ/weight-space-programming) (Tools, Harnesses and Agent Skills)
- **2026-11-05** · [Can GPT-6 Astra read and write GPT-2's weights?](https://github.com/AlexBodner/wsp-scaling) (Reading and predicting from weights)
- **2026-11-05** · [Rethinking Weight-Space Programming](https://github.com/ZhangYiqun018/rethinking-weight-space-programming) (Analyses and Critiques)
- **2026-11-05** · [Opus 5.5 makes π0.5 move faster and smoother by editing its weights](https://cuzyoung.github.io/robotics-weight-editing/en/) (Vision-language-action models)
- **2026-11-05** · [wsp-lab: cross-editor stress test of weight-space programming](https://github.com/WKJBryan/wsp-lab) (RL control policies)
- **2026-11-05** · [WeightLoop: Weight-Space Programming with Experimental Feedback](https://arxiv.org/abs/2611.07319) (Other Domains)

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
- [🧩 Other Domains](#-other-domains) (5)
- [🎮 Games](#-games) (5)
- [📊 Benchmarks and Evaluations](#-benchmarks-and-evaluations) (2)
- [🛠️ Tools, Harnesses and Agent Skills](#-tools-harnesses-and-agent-skills) (9)
- [🔍 Analyses and Critiques](#-analyses-and-critiques) (6)
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

- **[Weight-Space Programming for the Social Safety Net](https://github.com/ctrimm/weight-space-programming)**  
  ctrimm · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/ctrimm/weight-space-programming)] ![GitHub stars](https://img.shields.io/github/stars/ctrimm/weight-space-programming?style=social)  
  Tests whether an LLM can write, with no training, the exact weights of small networks computing four simplified US benefit formulas (SNAP, EITC, SSI, Medicaid). Three of four match the formula to within a trillionth of a dollar; the EITC network differs at one point by 2.4 cents. Trained networks are off by dollars.

- **[Weight-space programming on a clinical splicing model](https://github.com/KristinaMruts/weight-space-programming-spliceai)**  
  KristinaMruts · *GitHub* · 2026-11-04 · `💻 code / results`  
  [[Code](https://github.com/KristinaMruts/weight-space-programming-spliceai)] ![GitHub stars](https://img.shields.io/github/stars/KristinaMruts/weight-space-programming-spliceai?style=social)  
  Claude Opus 5.5 hand-edits 165 weights of OpenSpliceAI-MANE-10000nt to separate pathogenic from benign ClinVar variants. Hidden-test AUPRC 0.9385 → 0.9746. A temperature-only control gives 0.9695 and gradient fine-tuning of the same layers 0.9697-0.9710; authors conclude the edit matched ordinary training rather than beating it.

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
  U. Colorado Boulder · *NIPS 1991* · 1992 · `📄 peer-reviewed`  
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
  U. Wisconsin–Madison · *NIPS 1995* · 1996 · `📄 peer-reviewed` · 600 citations (OA)  
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
  AT&T Bell Laboratories · *NIPS 1989* · 1990 · `📄 peer-reviewed` · 3.2k citations (OA)  
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
  Stanford University / Ricoh California Research Center · *NIPS 1992* · 1993 · `📄 peer-reviewed` · 1.5k citations (OA)  
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
  Jonathan Frankle, Michael Carbin · *ICLR 2019* · 2018-03 · `📄 peer-reviewed` · 2k citations (OA)  
  [[Paper](https://arxiv.org/abs/1803.03635)]  
  Proposes that dense, randomly initialized networks contain subnetworks that reach comparable test accuracy when trained in isolation. Finds winning tickets under 10-20% of the size of fully-connected and convolutional networks on MNIST and CIFAR10.

- **[Are Sixteen Heads Really Better than One?](https://arxiv.org/abs/1905.10650)**  
  CMU + Facebook AI Research · *NeurIPS 2019* · 2019-05 · `📄 peer-reviewed` · 450 citations (OA)  
  [[Paper](https://arxiv.org/abs/1905.10650)]  
  Observes that a large percentage of attention heads can be removed at test time without significantly impacting performance, and some layers can be reduced to a single head. Also examines greedy pruning algorithms.

- **[Optimal Brain Compression: A Framework for Accurate Post-Training Quantization and Pruning](https://arxiv.org/abs/2208.11580)**  
  IST Austria · *NeurIPS 2022* · 2022-08 · `📄 peer-reviewed` · 85 citations (OA)  
  [[Paper](https://arxiv.org/abs/2208.11580)]  
  Introduces a framework covering weight pruning and quantization in the one-shot, post-training setting. It is built on an exact and efficient realization of the Optimal Brain Surgeon framework, extended to quantization.

- **[SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot](https://arxiv.org/abs/2301.00774)**  
  IST Austria · *ICML 2023* · 2023-01 · `📄 peer-reviewed` · 204 citations (OA)  
  [[Paper](https://arxiv.org/abs/2301.00774)]  
  Prunes GPT-family models in one shot without retraining. Runs on OPT-175B and BLOOM-176B in under 4.5 hours, reaching 60% unstructured sparsity with negligible perplexity increase, ignoring more than 100 billion weights.

- **[A Simple and Effective Pruning Approach for Large Language Models (Wanda)](https://arxiv.org/abs/2306.11695)**  
  CMU, Meta AI, Bosch Center for AI · *ICLR 2024* · 2023-06 · `📄 peer-reviewed` · 302 citations (OA)  
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
  University of Amsterdam · *EMNLP 2021* · 2021-04 · `📄 peer-reviewed` · 232 citations (OA)  
  [[Paper](https://arxiv.org/abs/2104.08164)]  
  Trains a hyper-network with constrained optimization to predict the weight update that changes one fact without affecting other knowledge. Tests it on a BERT fact-checking model and a BART question-answering model, with paraphrases changing consistently.

- **[Knowledge Neurons in Pretrained Transformers](https://arxiv.org/abs/2104.08696)**  
  Peking University + Microsoft Research · *ACL 2022* · 2021-04 · `📄 peer-reviewed` · 804 citations (S2)  
  [[Paper](https://arxiv.org/abs/2104.08696)]  
  Introduces a knowledge attribution method that identifies neurons expressing a relational fact in BERT on cloze tasks. Finds their activation correlates positively with the fact's expression, and case studies update and erase facts without fine-tuning.

- **[Fast Model Editing at Scale](https://arxiv.org/abs/2110.11309)**  
  Stanford · *ICLR 2022* · 2021-10 · `📄 peer-reviewed` · 195 citations (OA)  
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
  Stanford · *ICML 2022* · 2022-06 · `📄 peer-reviewed` · 64 citations (OA)  
  [[Paper](https://arxiv.org/abs/2206.06520)]  
  Introduces SERAC, which stores edits in an explicit memory and learns to reason over them to modulate the base model's predictions. Adds three editing problems on question answering, fact-checking and dialogue; only SERAC performs well on all three.

- **[Mass-Editing Memory in a Transformer (MEMIT)](https://arxiv.org/abs/2210.07229)**  
  Kevin Meng, Arnab Sen Sharma, Alex Andonian, Yonatan Belinkov, David Bau · *ICLR 2023* · 2022-10-13 · `📄 peer-reviewed` · 1.3k citations (S2)  
  [[Paper](https://arxiv.org/abs/2210.07229)] [[Code](https://github.com/kmeng01/memit)] [[Project](https://memit.baulab.info/)] ![GitHub stars](https://img.shields.io/github/stars/kmeng01/memit?style=social)  
  Extends ROME to thousands of edits at once across several layers.

- **[Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models](https://arxiv.org/abs/2301.04213)**  
  Google Research + UNC Chapel Hill · *NeurIPS 2023* · 2023-01 · `📄 peer-reviewed` · 44 citations (OA)  
  [[Paper](https://arxiv.org/abs/2301.04213)]  
  Shows that causal-tracing localization conclusions do not indicate which MLP layer is best to edit to override a stored fact. Also studies erasing and amplifying facts, where the edited layer predicts performance better than localization does.

- **[Unified Concept Editing in Diffusion Models](https://arxiv.org/abs/2308.14761)**  
  Northeastern/MIT/Technion · *WACV 2024* · 2023-08 · `📄 peer-reviewed` · 499 citations (S2)  
  [[Paper](https://arxiv.org/abs/2308.14761)]  
  Presents UCE, which edits text-to-image diffusion models without training, using a closed-form solution on text-conditional projections. Demonstrates simultaneous debiasing, style erasure and content moderation, with improved efficacy and scalability over prior work.

- **[AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://arxiv.org/abs/2410.02355)**  
  USTC + National University of Singapore · *ICLR 2025* · 2024-10 · `📄 peer-reviewed` · 52 citations (OA)  
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
  Thurnherr, Riesen · *Preprint* · 2024-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2410.00061)]  
  Generates a dataset of transformer-weight and RASP-program pairs with Tracr, then trains a model to recover RASP code from weights. Reproduces over 30% of test programs exactly; over 70% of outputs are functionally equivalent.

- **[A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090)**  
  Xiaolong Han et al. · *Preprint* · 2026-03-10 · `📝 preprint`  
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
  Alexander Matt Turner et al. · *Preprint* · 2023-08-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2308.10248)]  
  Adds a direction computed from contrasting prompts to the residual stream at inference.

- **[Representation Engineering: A Top-Down Approach to AI Transparency](https://arxiv.org/abs/2310.01405)**  
  Andy Zou et al. · *Preprint* · 2023-10-02 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2310.01405)] [[Code](https://github.com/andyzoujm/representation-engineering)] ![GitHub stars](https://img.shields.io/github/stars/andyzoujm/representation-engineering?style=social)  
  Reads and controls high-level concepts through population-level directions in representations.

- **[Steering Llama 2 via Contrastive Activation Addition (CAA)](https://arxiv.org/abs/2312.06681)**  
  Nina Rimsky et al. · *ACL 2024* · 2023-12-09 · `📄 peer-reviewed`  
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
  Zachary Coalson et al. · *Preprint* · 2024-12 · `📝 preprint`  
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
  Jonathan Raiman, Susan Zhang, Christy Dennison · *Preprint* · 2019-12 · `📝 preprint` · 2 citations (OA)  
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
  Swann, McGranahan, Buurmeijer, Kennedy, Schwager · *CoRL 2026* · 2026-03 · `📄 peer-reviewed`  
  [[Paper](https://arxiv.org/abs/2603.19183)] [[Code](https://github.com/swannaiden/drvla)] ![GitHub stars](https://img.shields.io/github/stars/swannaiden/drvla?style=social)  
  SAEs on π0.5 and OpenVLA: amplifying general features induces matching behavior and ablating them destroys performance, but most features are episode-specific memorization.

- **[Contrastive Conceptor Activation Steering (COAST): Unlocking Vision-Language-Action Models through Hidden States](https://arxiv.org/abs/2605.17144)**  
  Miranda Muqing Miao, Subin Kim, Brandon Yang, Lyle Ungar · *Preprint* · 2026-05 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2605.17144)]  
  Training-free conceptor steering of a VLA's action-expert residual stream (GR00T N1.5), learned from a few success and failure rollouts.

- **[Robotic Policy Adaptation via Weight-Space Meta-Learning (WIZARD)](https://arxiv.org/abs/2606.07217)**  
  Christian Bianchi et al. · *Preprint* · 2026-06 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2606.07217)]  
  A meta-network turns language and video into LoRA weights for a frozen VLA, with no test-time optimization.

- **[Steering Robustness into World Action Models via Mechanistic Interpretability and Optimal Control (WA-LQR)](https://arxiv.org/abs/2607.14943)**  
  *Preprint* · 2026-07 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.14943)]  
  Closed-loop LQR activation steering of Cosmos-Policy, DiT4DiT and LingBot-VA under camera, gripper and noise perturbations. Linear separability predicts which models can be steered.

- **[DiMaS: Distribution Matching for Steering Vision-Language-Action Models](https://arxiv.org/abs/2607.14280)**  
  Khayatan, Meziane, Parekh, Cord · *Preprint* · 2026-07 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.14280)] [[Code](https://github.com/pegah-kh/dimas)] ![GitHub stars](https://img.shields.io/github/stars/pegah-kh/dimas?style=social)  
  In flow-matching VLAs, behavioral features are linearly decodable but not linearly steerable, which motivates distribution matching instead.

- **[Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts (DART)](https://arxiv.org/abs/2607.00666)**  
  Taewook Kang, Taeheon Kim, Donghyun Shin, Jonghyun Choi · *Preprint* · 2026-07-01 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.00666)]  
  Adapts a VLA to camera and embodiment shifts from one demonstration through weight-vector arithmetic with subspace alignment.

- **[Suppression Sticks, Locality Is Fragile: A Closed-Loop Audit of Task-Vector Negation in VLA Policies](https://arxiv.org/abs/2608.04692)**  
  Wang, Guo, Dai, Zhao, Guo, Xiong · *Preprint* · 2026-08 · `📝 preprint`  
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

## Legend

`📄 peer-reviewed` · `📝 preprint` · `💻 code / results` · `💬 post only`

Entries are newest first within each section, except historical sections, which read oldest first. Summaries report the source's own numbers and settings. Evidence labels say what kind of source backs an entry, not whether its claims hold. Citation counts, where shown, are from Semantic Scholar (S2) or OpenAlex (OA) at the time the entry was added; the two sources are not comparable, so read them as orders of magnitude.

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
