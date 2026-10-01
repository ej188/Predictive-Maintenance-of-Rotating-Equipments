"""Render a wholly invented educational fixture, not company/model results.

Optional dependency: matplotlib. Run from the repository root with:
    python3 examples/plot_evaluation_slices.py
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from evaluation_slices import invented_rows, metrics


def main():
    rows = invented_rows()
    slices = [rows, [r for r in rows if r[0] > 3], [r for r in rows if r[0] <= 3]]
    values = [metrics(sample) for sample in slices]
    labels = ['Overall\n(n=100)', 'Reference > 3\n(n=90)', 'Reference ≤ 3\n(n=10)']
    colors = ['#475569', '#2563eb', '#d97706']
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.3))
    fig.suptitle('SYNTHETIC EXAMPLE — NOT INTERNSHIP RESULTS', fontsize=15, fontweight='bold', y=.97)
    for ax, index, title in zip(axes, [1, 3], ['Mean absolute error', 'Mean signed error (bias)']):
        heights = [v[index] for v in values]
        bars = ax.bar(labels, heights, color=colors, width=.62)
        ax.bar_label(bars, labels=[f'{h:.2f}' for h in heights], padding=5, fontsize=12)
        ax.set_title(title, pad=16)
        ax.set_ylabel('Arbitrary reference-target units')
        ax.set_ylim(0, 9.3)
        ax.set_axisbelow(True)
        ax.grid(axis='y', color='#e2e8f0')
        ax.spines[['top', 'right']].set_visible(False)
    fig.text(.5, .105, 'Invented values: a small near-end slice has much larger overprediction.', ha='center', fontsize=11)
    fig.text(.5, .055, 'Slices use retrospective reference targets; they are not an inference-time alert policy.', ha='center', fontsize=10, color='#475569')
    fig.subplots_adjust(top=.8, bottom=.27, wspace=.32, left=.075, right=.98)
    destination = Path(__file__).resolve().parent / 'figures' / 'synthetic-evaluation-slices.png'
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination, dpi=180, facecolor='white', metadata={'Title': 'Wholly synthetic evaluation fixture', 'Description': 'No company measurements, images, or model results.'})
    plt.close(fig)
    print(destination)


if __name__ == '__main__':
    main()
