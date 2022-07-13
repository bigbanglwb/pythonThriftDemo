struct message
{
	1:i32 seqId,
	2:string content
}

service Transmit
{
	void put(1:message msg)
}