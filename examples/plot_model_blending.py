"""Independent illustrative model-blending plot. No private image/data/code inputs.

Run with Python and matplotlib. Output goes to docs/figures. Run from the repository root: python3 examples/plot_model_blending.py
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from math import isclose

OUT = Path(__file__).resolve().parents[1] / 'docs' / 'figures'
COLORS = {'blue': '#2563eb', 'orange': '#d97706', 'dark': '#334155'}
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10})


def finish(fig, filename, footer):
    fig.text(.5, .045, footer, ha='center', fontsize=9, color='#475569')
    fig.subplots_adjust(top=.78, bottom=.21, left=.09, right=.96, wspace=.36)
    fig.savefig(OUT / filename, dpi=170, facecolor='white', metadata={'Description':'Invented educational example; no company data or original image pixels.'})
    plt.close(fig)


def blending():
    t = [i / 100 for i in range(101)]
    local_weight = [x ** 1.5 for x in t]
    historical_weight = [1 - w for w in local_weight]
    historical = [12.5 - 4*x for x in t]
    local = [13 - 12*x for x in t]
    blend = [wa*a + wb*b for wa,wb,a,b in zip(historical_weight,local_weight,historical,local)]
    assert all(isclose(a+b,1) for a,b in zip(historical_weight,local_weight))
    assert all(min(a,b)<=c<=max(a,b) for a,b,c in zip(historical,local,blend))
    fig, axes = plt.subplots(1,2,figsize=(11,4.8))
    fig.suptitle('ILLUSTRATIVE MODEL BLENDING — NOT INTERNSHIP RESULTS',fontsize=13,fontweight='bold',y=.97)
    axes[0].plot(t,historical_weight,label='Historical-cycle weight',color=COLORS['blue'],lw=2)
    axes[0].plot(t,local_weight,label='Current-cycle weight',color=COLORS['orange'],lw=2)
    axes[0].set(title='Invented weighting rule',xlabel='Illustrative cycle progress (0–1)',ylabel='Mixture weight',ylim=(-.03,1.03))
    axes[1].plot(t,historical,label='Historical-cycle estimate',color=COLORS['blue'],ls='--')
    axes[1].plot(t,local,label='Current-cycle estimate',color=COLORS['orange'],ls='--')
    axes[1].plot(t,blend,label='Combined estimate',color=COLORS['dark'],lw=2.5)
    axes[1].set(title='Weighted combination of two estimates',xlabel='Illustrative cycle progress (0–1)',ylabel='Illustrative RUL (arbitrary units)')
    for ax in axes:
        ax.grid(color='#e2e8f0');ax.spines[['top','right']].set_visible(False);ax.legend(frameon=False,fontsize=9)
    finish(fig,'illustrative-model-blending.png','All curves and the weighting rule are invented. This illustrates a concept, not the original blending algorithm or accuracy.')



if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    blending()
    print('Rendered invented model-blending illustration; mixture checks passed.')
