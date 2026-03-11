select
    order_id,
    customer_id,
    product_id,
    sum(amount) as revenue
from {{ ref('stg_orders') }}
group by 1,2,3