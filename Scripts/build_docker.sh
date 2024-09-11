clear


version=$(python3 buildUtls.py ver)
build_time=$(python3 buildUtls.py time)

echo
echo
echo 'Build and docker image and increase version'
echo Version      : $version
echo Build time   : $build_time
echo
echo

#=======================================

echo
echo '=== BUILD ==='
echo
docker build --build-arg BUILD_VERSION=${version}  --build-arg BUILD_TIME=${build_time}  -t gpu_monitor:$version ../.
echo
docker tag gpu_monitor:$version gpu_monitor:latest
#docker tag $image_name:$version $repo_adr/$image_name:latest
#docker tag $image_name:$version $repo_adr/$image_name:$version
#docker push $repo_adr/$image_name:$version
#docker push $repo_adr/$image_name:latest



#docker run -it rr_sync:latest
#docker run -it rr_sync:dev