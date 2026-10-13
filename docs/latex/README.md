# KissanVision LaTeX Academic Report & SRS

This directory contains the production-grade LaTeX source code for the **25-Page Project Report & Software Requirements Specification (SRS)** conforming to the UPES School of Computer Science B.Tech Data Science guidelines and IEEE Std 830-1998 / ISO/IEC/IEEE 29148:2018.

## File Contents
- **`main.tex`**: The complete, self-contained master LaTeX source document encompassing:
  - Cover page, Candidates' Declaration, Certificate, Acknowledgement, Abstract, Version History
  - Automated Table of Contents, List of Figures, List of Tables
  - **Part I: Project Report** (Chapters 1 to 7 + 30 IEEE References)
  - **Part II: Software Requirements Specification** (Revision History, Sections 1 to 3, Glossary, Analysis Models, and Issues List)
  - Embedded TikZ vector diagrams (Iterative process cycle, architecture block diagram, Level-0 DFD context diagram)
  - Problem statement callout boxes and algorithm environment boxes
  - Mathematical formulations for XGBoost, SHAP TreeExplainer, and evaluation metrics

## How to Compile

### Option 1: On Overleaf (Recommended & Fastest)
1. Go to [Overleaf](https://www.overleaf.com/).
2. Click **New Project** $\rightarrow$ **Blank Project** (or **Upload Project**).
3. Upload `main.tex` into the project root.
4. Set compiler to **pdfLaTeX** (default in Overleaf).
5. Click **Recompile**.
   - Your complete 20–25 page PDF with roman front matter and arabic body pagination will be generated instantly.

### Option 2: Local Compilation (TeX Live, MiKTeX, MacTeX)
Run `pdflatex` twice to resolve cross-references, table of contents, and figure/table counters:

```bash
cd docs/latex
pdflatex main.tex
pdflatex main.tex
```

### Required Packages (All Standard in TeX Live / Overleaf)
- `geometry`, `graphicx`, `amsmath`, `amssymb`, `booktabs`, `tabularx`, `array`, `longtable`, `multirow`
- `fancyhdr`, `titlesec`, `tikz`, `tcolorbox`, `hyperref`, `xcolor`
