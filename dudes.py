{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "import numpy as np \n",
    "import seaborn as sns \n",
    "import matplotlib.pyplot as plt "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.DataFrame({\"name\":np.random.choice([\"John\",\"Kris\",\"George\"],100),\"age\":np.random.randint(12,60,100),\"salary\":np.random.randint(800,2000,100)})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>name</th>\n",
       "      <th>age</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Kris</td>\n",
       "      <td>37</td>\n",
       "      <td>1280</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>George</td>\n",
       "      <td>22</td>\n",
       "      <td>1683</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Kris</td>\n",
       "      <td>42</td>\n",
       "      <td>1819</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>John</td>\n",
       "      <td>12</td>\n",
       "      <td>925</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Kris</td>\n",
       "      <td>21</td>\n",
       "      <td>890</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     name  age  salary\n",
       "0    Kris   37    1280\n",
       "1  George   22    1683\n",
       "2    Kris   42    1819\n",
       "3    John   12     925\n",
       "4    Kris   21     890"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x=\"name\",y=\"age\",data=data,ci=False)\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.2 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "4d8546321cadb325a106918ecab26f0085318f6086fcab55f85fe19b56b4f4f0"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
