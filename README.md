# Post-Quantum Cryptography in n-Dimensional Geometries

## Overview / Обзор

This repository presents a reproducible cryptographic framework based on high-dimensional rotation groups: SU(n), SO(n), and quaternionic structures. It includes generators, tests, and documentation for post-quantum primitives designed to resist quantum attacks.

Данный репозиторий содержит воспроизводимую криптографическую систему, основанную на многомерных группах вращения SU(n), SO(n) и кватернионных структурах. Включены генераторы, тесты и документация для постквантовых примитивов, устойчивых к квантовым атакам.

## Structure / Структура

- `src/` — generators and core algorithms
- `docs/` — conceptual documentation
- `tests/` — verification of matrix properties
- `LICENSE` — MIT license
- `metadata.json` — Zenodo metadata

## Citation / Цитирование

If you use this project in your research, please cite it via Zenodo:

**DOI**: [10.5281/zenodo.17170276](https://doi.org/10.5281/zenodo.17170276)
# Post-Quantum ND Crypto

Криптографический протокол на основе многомерной геометрии и групп SO(n), SU(n).  
Устойчив к квантовым атакам, построен на инвариантных преобразованиях и ортогональных структурах.

## 📐 Теоретическая основа

- Группы: SO(n), SU(n), G₂, F₄
- Геометрия: n-мерные ортогональные пространства
- Преобразования: инвариантные, обратимые, устойчивые к декодированию

## 📦 Состав проекта

- `src/` — исходный код протокола
- `docs/` — документация и публикационные материалы
- `LICENSE` — MIT
- `README.md` — описание и структура

## 🧪 Тестирование

```bash
python src/test_nd.py
