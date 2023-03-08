select users.id, COUNT(posts.id)
from posts RIGHT JOIN users ON
posts.owner_id = users.id group by users.id;

select posts.* , count(votes.post_id) as numberofvotes from posts LEFT JOIN votes on posts.id = votes.post_id
group by posts.id