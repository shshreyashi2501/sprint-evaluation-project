resource "aws_s3_bucket" "demo" {
  bucket = "devsecops-demo-bucket-12345"
  acl    = "public-read"   # ❌ vulnerability
}