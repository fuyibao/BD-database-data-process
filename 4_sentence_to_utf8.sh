for i in *txt
do
echo $i 
name=$(basename $i .txt)
trans=$name"_utf8"".txt"
java -jar replace_utf8.jar $i > ~/Process_NCBI_article/2018Fulltext_after_utf8/$trans
done
