import pickle 
import numpy as np 
import streamlit as sl

sl.header("Book Recommendation System using Collaborative Filtering")

model = pickle.load(open('artifacts/model.pkl','rb'))
books_name = pickle.load(open('artifacts/names_of_books.pkl','rb'))
books_with_ratings = pickle.load(open('artifacts/books_with_ratings.pkl','rb'))
book_pivot_table = pickle.load(open('artifacts/book_pivot_table.pkl','rb'))

selected_book = sl.selectbox(
    "Type or select the name of the book you're currently reading.", books_name)

def fetch_poster(suggestion):
    book_names = []
    book_id_index =[]
    poster_url =[]

    for book_id in suggestion:
        book_names.append(book_pivot_table.index[book_id])
    
    for name in book_names[0]:
        id = np.where(books_with_ratings['Title'] == name)[0][0]
        book_id_index.append(id)

    for idx in book_id_index:
        url = books_with_ratings.iloc[idx]['Img_url']
        poster_url.append(url)

    return poster_url

def recommend_books(book_name):
    book_list=[]
    book_id = np.where(book_pivot_table.index == book_name)[0][0]
    #this will only return the numerical index of the book.
    distance, suggestion = model.kneighbors(book_pivot_table.iloc[book_id,:].values.reshape(1,-1),
                                            n_neighbors=10)
    
    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot_table.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    return book_list,poster_url
    


if sl.button('Show Recommendation'):
    recommendation_books, poster_url= recommend_books(selected_book)
    col1,col2,col3,col4,col5 = sl.columns(5)
    col6,col7,col8,col9= sl.columns(4)

    with col1:
        sl.markdown(recommendation_books[1])
        sl.image(poster_url[1])
    
    with col2:
        sl.markdown(recommendation_books[2])
        sl.image(poster_url[2])
    
    with col3:
        sl.markdown(recommendation_books[3])
        sl.image(poster_url[3])

    with col4:
        sl.markdown(recommendation_books[4])
        sl.image(poster_url[4])
    
    with col5:
        sl.markdown(recommendation_books[5])
        sl.image(poster_url[5])
    
    with col6:
        sl.markdown(recommendation_books[6])
        sl.image(poster_url[6])
    
    with col7:
        sl.markdown(recommendation_books[7])
        sl.image(poster_url[7])
    
    with col8:
        sl.markdown(recommendation_books[8])
        sl.image(poster_url[8])
    
    with col9:
        sl.markdown(recommendation_books[9])
        sl.image(poster_url[9])
    
    # with col10:
    #     sl.text(recommendation_books[10])
    #     sl.image(poster_url[10])
