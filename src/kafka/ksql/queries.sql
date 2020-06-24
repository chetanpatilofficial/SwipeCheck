/* create user location stream */
CREATE STREAM user_location 
  (user_id VARCHAR, 
   t_time_stamp VARCHAR, 
   t_millis INTEGER, 
   latitude DOUBLE, 
   longitude DOUBLE) 
  WITH (KAFKA_TOPIC='location01', 
        VALUE_FORMAT='DELIMITED');

/* create transaction location stream */
CREATE STREAM transaction_location 
  (merchant_id VARCHAR, 
   user_id VARCHAR, 
   t_time_stamp VARCHAR, 
   t_millis INTEGER, 
   amount VARCHAR, 
   latitude DOUBLE, 
   longitude DOUBLE) 
  WITH (KAFKA_TOPIC='transaction01',
        VALUE_FORMAT='DELIMITED');

/* create stream by combining user and transaction location stream */
CREATE STREAM COMBINED_TRANSACTION_LOCATION_1 AS 
	SELECT tloc.user_id as user_id, 
			uloc.user_id as uloc_user_id,
			tloc.merchant_id as merchant_id, 
			tloc.t_time_stamp as transaction_time, 
			tloc.t_millis as transaction_millis, 
			tloc.amount as amount, 
			tloc.latitude as tloc_latitude, 
			tloc.longitude as tloc_longitude, 
			uloc.t_time_stamp as user_location_time, 
			uloc.t_millis as user_location_millis, 
			uloc.latitude as uloc_latitude, 
			uloc.longitude as uloc_longitude, 
			GEO_DISTANCE(tloc.latitude, tloc.longitude, uloc.latitude, uloc.longitude, 'KM') as distance
	FROM transaction_location tloc INNER JOIN user_location uloc WITHIN 10 MINUTES
	ON tloc.user_id = uloc.user_id;
