CREATE TABLE COMBINED_TRANSACTION_LOCATION 
	(tloc_user_id TEXT NOT NULL, 
	uloc_user_id TEXT NOT NULL, 
	merchant_id TEXT NOT NULL, 
	t_time_stamp TIMESTAMPTZ NOT NULL, 
	t_millis NUMERIC NOT NULL, 
	amount FLOAT NOT NULL, 
	tloc_latitude DOUBLE PRECISION NOT NULL, 
	tloc_longitude DOUBLE PRECISION NOT NULL, 
	u_time_stamp TIMESTAMPTZ NOT NULL, 
	u_millis NUMERIC NOT NULL, 
	uloc_latitude DOUBLE PRECISION NOT NULL, 
	uloc_longitude DOUBLE PRECISION NOT NULL, 
	distance FLOAT NOT NULL);

SELECT create_hypertable('COMBINED_TRANSACTION_LOCATION', 't_time_stamp');


