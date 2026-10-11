# AutoEDA 🚀

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![CLI Framework](https://img.shields.io/badge/CLI-Click-brightgreen.svg)](https://click.palletsprojects.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTION.md)
[![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

> **Lightning-fast Exploratory Data Analysis directly in your terminal.**  
> Powered by Python & [Click](https://click.palletsprojects.com/). Zero boilerplate. Zero notebooks. No need to write Pandas scripts just to inspect your data.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Why AutoEDA?](#-why-autoeda)
- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [Supported Formats](#-supported-formats)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [CLI Command Reference](#-cli-command-reference)
- [Architecture & Design Philosophy](#-architecture--design-philosophy)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [Code of Conduct](#-code-of-conduct)
- [License](#-license)

---

## 💡 Overview

**AutoEDA** is an open-source, terminal-native CLI utility built in **Python** using the **[Click](https://click.palletsprojects.com/)** framework to streamline Exploratory Data Analysis (EDA). 

In traditional data workflows, inspecting a new dataset requires launching a heavy Jupyter notebook or writing repetitive Python scripts using libraries such as `pandas`, `seaborn`, and `matplotlib`. AutoEDA eliminates this friction: with a single terminal command, you get comprehensive statistics, missing value audits, outlier alerts, correlation insights, and beautiful terminal visualizations in milliseconds.

```bash
# Get an instant, comprehensive overview of your dataset
autoeda overview data.csv
```

---

## 🛠 Tech Stack

- **Core Runtime:** Python 3.8+
- **CLI Framework:** **[Click](https://click.palletsprojects.com/)** — powers nested command groups, automatic help page formatting, robust option parsing, argument types, and exit code handling.
- **Terminal UI & Styling:** Terminal styling, color palettes, and Unicode tables for rich CLI output.
- **Data Ingestion & Computation:** High-throughput streaming and chunked numerical computation engines.

---

## ⚡ Why AutoEDA?

| Scenario | Traditional Workflow | With AutoEDA 🚀 |
| :--- | :--- | :--- |
| **Initial Inspection** | Open notebook, import `pandas`, `df.head()`, `df.info()`, `df.describe()` | `autoeda overview data.csv` |
| **Missing Values** | `df.isnull().sum()`, plot missingness heatmap | `autoeda missing data.csv --plot` |
| **Distributions** | Write matplotlib/seaborn code, configure subplots | `autoeda stats data.csv --hist` |
| **Correlations** | `df.corr()`, plot seaborn heatmap with annot | `autoeda correlate data.csv` |
| **Reports** | Write report scripts or use heavy HTML profiling tools | `autoeda report data.csv -o report.html` |
| **Workflow Speed** | 5 - 15 minutes setup & coding | **Instant (sub-second execution)** |

---

## ✨ Key Features

- **📊 Instant Dataset Diagnostics:**
  - Fast summary of dataset shape, column types, memory footprint, and duplicate rows.
  - Automatic detection of numerical, categorical, datetime, and text features.

- **📈 Deep Statistical Profiles:**
  - Parametric and non-parametric stats: Mean, Median, Mode, Standard Deviation, Variance, Skewness, Kurtosis, and IQR.
  - Min/Max, 25th, 50th, and 75th percentiles.

- **🔍 Missing Data Audits:**
  - Per-column missing counts and percentage breakdown.
  - Visual terminal-based missing data density charts and flags for high null counts.

- **📉 Terminal Visualizations:**
  - Colorized ANSI/Unicode histograms, sparklines, and boxplots rendered right in your terminal window.
  - Interactive terminal pagination (`--pager`) for large datasets and wide column lists.

- **🔗 Correlation Matrix & Collinearity Detection:**
  - Pearson, Spearman, and Kendall rank correlation metrics.
  - Highlighting collinear pairs that could cause issues in downstream machine learning models.

- **🚨 Outlier Identification:**
  - Flag anomalies using Tukey's IQR rule and Z-score thresholds without manual filtering.

- **📑 Shareable Reports:**
  - Export rich, standalone, interactive HTML reports or lightweight Markdown summaries for team documentation and CI pipelines.

---

## 📂 Supported Formats

AutoEDA natively ingests common structured data formats:
- **CSV / TSV** (`.csv`, `.tsv`)
- **Parquet** (`.parquet`)
- **JSON / JSON Lines** (`.json`, `.jsonl`)
- **Excel** (`.xlsx`, `.xls`)
- **Feather / Arrow** (`.feather`, `.arrow`)

---

## 📦 Installation

### Option 1: Using pip (Recommended once published)
```bash
pip install autoeda
```

### Option 2: Using pipx (Isolated CLI environment)
```bash
pipx install autoeda
```

### Option 3: From Source (Development)
```bash
# Clone the repository
git clone https://github.com/GFG-OS-MANAGEMENT/AutoEDA.git

# Navigate into the project directory
cd AutoEDA

# Create and activate virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```

---

## 🚀 Quick Start

Here are common ways to use AutoEDA from your terminal:

### 1. High-Level Dataset Overview
Inspect row/column counts, memory usage, and column data types:
```bash
autoeda overview dataset.csv
```

*Sample Output:*
```text
┌──────────────────────────────────────────────────────────┐
│                   AutoEDA: Dataset Overview              │
├──────────────────────────────────────────────────────────┤
│ File: dataset.csv | Format: CSV | Size: 1.42 MB          │
│ Rows: 10,000      | Columns: 8  | Duplicates: 12         │
├──────────────────────────────────────────────────────────┤
│ Column Name      Type       Missing (%)   Distinct       │
│ id               Integer    0 (0.0%)      10,000         │
│ age              Integer    45 (0.45%)    68             │
│ department       String     0 (0.0%)      6              │
│ salary           Float      120 (1.20%)   3,412          │
│ join_date        Datetime   0 (0.0%)      1,240          │
└──────────────────────────────────────────────────────────┘
```

### 2. Comprehensive Column Statistics
Obtain summary metrics for numerical attributes:
```bash
autoeda stats dataset.csv --columns age,salary
```

### 3. Missing Value Analysis
Identify columns with missing data and see null density:
```bash
autoeda missing dataset.csv --threshold 5.0
```

### 4. Correlation Matrix
Generate a colorized correlation matrix in the terminal:
```bash
autoeda correlate dataset.csv --threshold 0.6
```

### 5. Generate Standalone HTML / Markdown Report
Create a full visual report that you can open in your browser or attach to pull requests:
```bash
# Export an interactive HTML report
autoeda report dataset.csv --format html --output report.html

# Export Markdown summary for documentation
autoeda report dataset.csv --format markdown --output eda_summary.md
```

---

## 🛠 CLI Command Reference

All commands are implemented as composable [Click](https://click.palletsprojects.com/) commands. You can append `--help` to any command for full usage details (e.g., `autoeda stats --help`).

| Command | Description | Example Flags |
| :--- | :--- | :--- |
| `autoeda overview <file>` | Display dataset shape, types, memory, and preview | `--head 5`, `--tail 5` |
| `autoeda stats <file>` | Compute summary statistics for numerical/categorical data | `--columns col1,col2`, `--hist` |
| `autoeda missing <file>` | Analyze missing values and missingness patterns | `--threshold <pct>`, `--plot` |
| `autoeda correlate <file>`| Calculate correlation matrix with terminal heatmaps | `--method pearson\|spearman`, `--min 0.5` |
| `autoeda outliers <file>` | Detect outliers using IQR or Z-score methods | `--method iqr\|zscore`, `--col <name>` |
| `autoeda cat <file>` | Distribution & frequency tables for categorical fields | `--top <n>`, `--cardinality` |
| `autoeda normalize <file>`| Scale numerical features (Min-Max, Standard Z-score, Robust, MaxAbs) | `--method standard\|minmax\|robust`, `-o <path>` |
| `autoeda transform <file>`| Transform features (Log, Box-Cox, Yeo-Johnson, Sqrt, Binning) | `--method log\|boxcox\|bin`, `--bins 5` |
| `autoeda pca <file>` | Principal Component Analysis, scree plot, loadings, projections | `--n-components 3`, `--scree`, `-o <path>` |
| `autoeda dist <file>` | Distribution profiling & normality tests (Shapiro-Wilk, K-S, Q-Q plot) | `--test shapiro\|ks\|all`, `--qq` |
| `autoeda vif <file>` | Multicollinearity diagnostics via Variance Inflation Factor (VIF) | `--threshold 5.0`, `--corr-threshold 0.8` |
| `autoeda time <file>` | Time series profiling (sampling cadence, gaps, ACF autocorrelation) | `--date-col timestamp`, `--lags 20` |
| `autoeda clean <group>` | Data cleaning suite (fill, drop, dedup, cast, rename, clip, encode) | `autoeda clean fill -s mean -o out.csv` |
| `autoeda report <file>` | Generate an exportable interactive or static report | `--format html\|md\|json`, `-o <path>` |

---

## 🏗 Architecture & Design Philosophy

AutoEDA is guided by three core design tenets:

1. **Click-Powered Modular CLI:** Every command is built with Python's `click` library, ensuring declarative options, automated bash/zsh autocomplete support, and intuitive `--help` screens.
2. **Terminal-First UX:** Rich color schemes, formatted unicode tables, and responsive rendering using modern terminal formatting.
3. **Performance & Memory Efficiency:** Built to handle larger-than-RAM files using streaming and chunked parsing without freezing your terminal.
4. **Zero Python Code Required for End Users:** The end user never needs to remember syntax like `pd.read_csv(...)`, `df.groupby(...)`, or plot styling APIs.

---

## 🗺 Roadmap

- [ ] **Interactive TUI Mode:** A curses/Textual-based full-screen terminal interface for live dataset browsing.
- [ ] **Direct SQL & Remote Storage:** Run EDA on SQLite, DuckDB, PostgreSQL, and AWS S3/GCS buckets directly.
- [ ] **LLM Dataset Insights:** Optional plugin for AI-generated plain English dataset summaries.
- [ ] **Automated Data Quality Warnings:** Automated checks for data drift, leakage risks, and skewed distributions.
- [ ] **Export to Jupyter Notebook:** Generate the equivalent python code as a ready-to-run `.ipynb` file.

---

## 🤝 Contributing

Contributions are warmly welcome! Whether you are fixing bugs, improving docs, adding new CLI commands via Click, or suggesting ideas, your help makes AutoEDA better for everyone.

Please read our [**CONTRIBUTION.md**](CONTRIBUTION.md) guide for details on our code of conduct, Click development guidelines, and pull request process.

---

## 📜 Code of Conduct

We are committed to fostering an open and welcoming community. All contributors and participants are expected to adhere to our [**CODE_OF_CONDUCT.md**](CODE_OF_CONDUCT.md).

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <b>Built with ❤️ by the open-source community at <a href="https://github.com/GFG-OS-MANAGEMENT">GFG OS Management</a></b>
</div>
