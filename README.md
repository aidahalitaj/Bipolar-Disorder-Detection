# Tweet-process

##Processing
 - Remove url

Input format `<userid>\t<tweet_content>`
Output  `<userid>\t<tweet_content_without_url>`

##Word count map_reduce


Input format `<userid>\t<tweet_content>`

Run the command below to do Word count
`cat <input_file> | ./lmr 8m 8 'python3 tweets_word_count_map.py' 'python3 tweets_word_count_reduce.py' <output_folder>`

Run the command below to merge the result to single file
`python image.py <map_reduce_result_folder> <result_folder>`

##Calculate Word Collocation

Input format `<userid>\t<tweet_content>`
Output  csv file and format is frequent col-location word set `<word1-word2>,<frequence>`

##Calculate Dataset Similarity (Cosine Similarity)

Base on **Collocation**, we getthe frequent col-location word set and corresponding frequence.
We do the normalization for each dataset vector based on their frequence, and calculate the Cosine Similarity.

* Autoamtic get the .csv file to be the input, which is the result of **Collocation** , csv format `<word1-word2>,<frequence>`
* Output similarity result on command line and csv file whose format is `<word>,<value of dataset1>,<value of dataset2>,<value of dataset3>...`