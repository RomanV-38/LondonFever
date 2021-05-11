<p style="text-align: center; font-size: 30px"> <b>London Fever</b></p>  
<p style="text-align: center; font-size: 20px"> <b>Projet Data Analyst BootCamp  
    <a href="https://datascientest.com/">Datascientest</a> </b></p>
    
<p style="font-size: 15px"> <b>Participants:</b> <br>  </p>
<ul>
<li> <a href="https://www.linkedin.com/in/roman-vuillaume" 
        class="social-icon si-rounded si-small si-linkedin">
     <i class="icon-linkedin"></i>
        Roman VUILLAUME</a>
</li>
<li> <a href="https://www.linkedin.com/in/charlie-paré" 
        class="social-icon si-rounded si-small si-linkedin">
     <i class="icon-linkedin"></i>
        Charlie PARÉ</a>
</li>
<li> <a href="https://fr.linkedin.com/in/smail-makoudi" 
        class="social-icon si-rounded si-small si-linkedin">
     <i class="icon-linkedin"></i>
        Smail MAKOUDI</a>
</li>
</ul>
<br><br>
<div style="font-size: 17px;">
    La <b>London Fire Brigade</b> (LFB) et ses 102 stations interviennent sur les incidents dans toute l'aire urbaine de Londres.
    <br>
    Elle dénombre en moyenne un peu plus de <b>150.000 interventions</b> de natures diverses (incendies, secours aux personnes, etc.) par an.
    <br>
    Le temps d'intervention des forces de secours est l'un des facteurs majeurs dans la mitigation des dégâts aux personnes et matériels.
    <br>
    Pour cette raison, le maintien d'un temps d'intervention des premiers secours en dessous de <b>360 secondes</b> est l'un des principaux objectifs de la LFB.
    <br>
    Pour ce projet nous allons nous intéresser aux données de la LFB et proposer un modèle de prédiction capable de déterminer <b>le temps moyen d'intervention des stations environnantes</b>,
    à une adresse dans l'aire urbaine de Londres.
</div>
<div style="font-size: 15px;">
Pour exécuter l'application en local :
<ul>
    <li>
    Lancez le serveur Bokeh dans un premier terminal : <code>bokeh serve bok_point_standalone.py</code>
   </li>
    <li>
    Lancez l'application streamlit dans un second terminal : <code>streamlit run main.py</code>
   </li>
    
</ul>
L'application streamlit s'attend à trouver le document Bokeh (Outil de Prédiction) à l'adresse : http://localhost:5006/ <br>
Si le serveur bokeh n'a pas démarré à cette adresse, vous devrez changer l'adresse manuellement dans src/bokeh_std.py
</div>