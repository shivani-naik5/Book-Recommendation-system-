#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import numpy as np

# Load pickled data
with open('pt.pkl', 'rb') as pt_file:
    pt = pickle.load(pt_file)
with open('books.pkl', 'rb') as books_file:
    books = pickle.load(books_file)
with open('similarity_score.pkl', 'rb') as similarity_file:
    similarity_score = pickle.load(similarity_file)

# Streamlit UI
st.title('Book Recommender')

# User input for book name
user_input = st.text_input('Enter a book name:', 'Book Title Here')

# Find index of the input book
try:
    index = np.where(books['Book-Title'] == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    # Display similar books
    st.header('Recommended Similar Books')
    for i, score in similar_items:
        book_title = books.iloc[i]['Book-Title']
        author = books.iloc[i]['Book-Author']
        image_url = books.iloc[i]['Image-URL-M']  # Assuming 'Image-URL-M' is the column with image URLs

        # Display book details and image
        st.write(f'{book_title} by {author}')
        if image_url:
            st.image(image_url, caption=book_title, use_column_width=True)
        else:
            st.write('Image not available')

except IndexError:
    st.warning('Book not found in the dataset.')

# Note: You may want to add additional checks and validation for user input.


# In[ ]:




