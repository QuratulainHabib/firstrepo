chilla=pd.read_csv("PYTHON_WITH_AMMAR")
print(chilla)

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks", color_codes=True)
p=sns.countplot(x="Gender", hue="Age", data=chilla)plt.show()
