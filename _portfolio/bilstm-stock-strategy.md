---
title: "BiLSTM Stock Forecasting & Dynamic Trading Strategy"
excerpt: "IEEE-published time-series research across 11 stocks, 8 sectors, and four rebalancing windows."
collection: portfolio
---

This peer-reviewed study compared LSTM and bidirectional LSTM models for stock-price forecasting, then tested whether the forecasts could support a dynamic portfolio-selection strategy. The experiments covered 11 stocks in 8 sectors and multiple training horizons.

## Research design

| | |
|---|---|
| **Question** | Can bidirectional sequence modeling improve stock forecasts and support a stronger dynamic allocation rule? |
| **Universe** | 11 stocks across 8 sectors |
| **Models** | LSTM and BiLSTM |
| **Horizons** | Six-month, one-year, and two-year training windows |
| **Strategy tests** | 3-day, 5-day, 7-day, and 14-day rebalancing |
| **Publication** | 2024 5th International Conference on Machine Learning and Human-Computer Interaction (MLHMI) |

The trading experiment began with a $100,000 portfolio. At each rebalancing point, the dynamic strategy used model forecasts to select a top-five portfolio and was compared with a static version of the portfolio.

## Strategy results

| Rebalancing window | Static comparison | Dynamic strategy |
|---|---:|---:|
| 3-day | $119,694 | **$123,630** |
| 5-day | $115,444 | **$117,425** |
| 7-day | $112,918 | **$126,078** |
| 14-day | $109,754 | **$123,306** |

The dynamic strategy finished above the static comparison in every tested window, with the largest differences in the 7-day and 14-day experiments. This wording replaces an earlier unsupported summary claim and reports only the outcomes shown in the paper.

## Interpretation and limitations

The project links model evaluation to a decision rule rather than stopping at forecast error. The results remain a historical simulation: they should be interpreted with market-regime, transaction-cost, and execution assumptions in mind and are not investment advice.

## Publication

**Jiayi Liu, Yufeng Yang, Teng Lin, Chuanhui Peng, and Yancong Deng.** “Enhancing Stock Price Forecasting and Trading Strategy through Bidirectional LSTM Integration.” *2024 5th International Conference on Machine Learning and Human-Computer Interaction (MLHMI)*, pp. 22–25.

- [Publication page](/publication/2024-03-14-bidirectional-lstm)
- [Read the paper](/files/TENG_JIAYI_YUFENG.pdf)
- [DOI: 10.1109/MLHMI63000.2024.00013](https://doi.org/10.1109/MLHMI63000.2024.00013)

**Attribution:** Teng Lin is a co-author of the five-author paper.
