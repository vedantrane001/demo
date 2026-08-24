{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dd783b72-8564-4003-8b54-24d9281636c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import sqlite3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "dafe4c51-6529-45ec-8642-e28a80ecac6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect to database\n",
    "conn = sqlite3.connect(\"../data/sales.db\")\n",
    "\n",
    "# Load data into dataframe\n",
    "df = pd.read_sql_query(\"SELECT * FROM sales\", conn)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "695caac5-bbf8-4c88-a276-c2f8e911a6d0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-11 10:19:06.277 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:06.285 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:06.798 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\vedan\\AppData\\Roaming\\Python\\Python313\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-11-11 10:19:06.800 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:06.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:06.813 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:06.824 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:06.826 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.set_page_config(page_title=\"📊 Sales Performance Dashboard\", layout=\"wide\")\n",
    "\n",
    "# Title and description\n",
    "st.title(\"📊 Sales Performance Dashboard\")\n",
    "st.markdown(\"Analyze company sales data to identify performance trends across regions, products, and categories.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "291dfeec-cbc3-4e90-945c-8603acb98448",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-11 10:19:30.127 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:30.130 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:30.131 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:30.180 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:30.181 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:19:30.184 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.subheader(\"🧾 Dataset Preview\")\n",
    "st.dataframe(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8b37603c-319b-4f79-929c-46039dce68ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-11-11 10:22:33.314 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:22:33.317 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:22:33.319 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:22:33.327 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:22:33.329 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-11-11 10:22:33.331 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.subheader(\"🧾 Dataset Preview\")\n",
    "st.dataframe(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53975906-93d8-45fe-94be-fa94236de6b7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
