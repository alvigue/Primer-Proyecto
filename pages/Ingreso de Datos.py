import streamlit as st 
st.logo("Imagenes\logo_ucg.png")
st.markdown("# Ingreso de Datos")
#
# Implementación de Widgets Interactivos
#
nombre 		= st.text_input('Nombres y Apellidos') 
edad 		= st.number_input('Edad', min_value=0, max_value=100, step=1) 
mes 		= st.slider('Seleccionar Mes', min_value=1, max_value=12, step=1) 
genero 		= st.radio('Género', ('Masculino', 'Femenino', 'Otro')) 
pais 		= st.selectbox('Selecciona tu País', ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Ecuador', 'Guyana' , 'Paraguay', 'Perú', 'Surinam', 'Uruguay','Venezuela']) 
fecha 		= st.date_input('Selecciona una Fecha') 
hora 		= st.time_input('Selecciona una Hora') 
archivo 	= st.file_uploader('Cargar Archivo') 
acepta_terminos = st.checkbox('Acepta Términos y Condiciones') 
#
# Guarda información ingresada
#
if st.button('Enviar Información'): 
	st.divider()
	st.write('Nombres y Apellidos:', nombre) 
	st.write('Edad:', edad) 
	st.write('Mes Seleccionado:', mes) 
	st.write('Género:', genero) 
	st.write('País:', pais) 
	st.write('Fecha Seleccionada:', fecha) 
	st.write('Hora Seleccionada:', hora) 
	st.write('Archivo Cargado:', archivo) 
	st.write('Acepta Términos:', acepta_terminos) 
st.divider()

