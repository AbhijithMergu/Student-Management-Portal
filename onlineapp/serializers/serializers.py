from rest_framework import serializers
from onlineapp.models import College,Student, MockTest1


class CollegeSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=128)
	location = serializers.CharField(max_length=64)
	acronym = serializers.CharField(max_length=8)
	contact = serializers.EmailField()

	def create(self, validated_data):
		return College.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.location = validated_data.get('location', instance.location)
		instance.acronym = validated_data.get('acronym', instance.acronym)
		instance.contact = validated_data.get('contact', instance.contact)
		instance.save()
		return instance


# class StudentSerializer(serializers.Serializer):
#
# 	id = serializers.IntegerField(read_only=True)
# 	name = serializers.CharField(max_length=128)
# 	dob = serializers.DateField(allow_null=True, required=False)
# 	db_folder = serializers.CharField(max_length=50)
# 	dropped_out = serializers.BooleanField(default=False)
# 	college = serializers.SlugRelatedField(
# 			read_only=True,
# 			slug_field='name'
# 		)
	# college = serializers.PrimaryKeyRelatedField(read_only=True)

	# college = CollegeSerializer()
	# def create(self, validated_data):
	# 	return College.objects.create(**validated_data)

# class StudentDetailSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	name = serializers.CharField(max_length=128)
# 	dob = serializers.DateField(allow_null=True, required=False)
# 	db_folder = serializers.CharField(max_length=50)
# 	dropped_out = serializers.BooleanField(default=False)
# 	college = serializers.SlugRelatedField(
#
# 	)


class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		exclude = []


class MockTest1Serializer(serializers.ModelSerializer):
	class Meta:
		model = MockTest1
		fields = ('problem1','problem2','problem3','problem4','total')

	def create(self, validated_data):
		data_copy = self._kwargs.get('data')
		data_copy.pop('total')
		validated_data['student'] = data_copy.pop('student')
		mocktest1 = MockTest1.objects.create(**validated_data)
		mocktest1.total = sum(data_copy.values())
		mocktest1.save()
		return mocktest1

	def update(self, instance, validated_data):
		instance.problem1 = validated_data.get('problem1', instance.problem1)
		instance.problem2 = validated_data.get('problem2', instance.problem2)
		instance.problem3 = validated_data.get('problem3', instance.problem3)
		instance.problem4 = validated_data.get('problem4', instance.problem4)
		validated_data.pop('total')
		instance.total = validated_data.get('total', sum(validated_data.values()))
		instance.save()
		return instance


class StudentDetailSerializer(serializers.ModelSerializer):
	mocktest1 = MockTest1Serializer(many=False)
	class Meta:
		model = Student
		fields = ('id','name','dob','email','db_folder','dropped_out','college','mocktest1')

	def create(self, validated_data):
		mocktest1_data = dict(validated_data.pop('mocktest1'))
		pk = self._kwargs.get('data').get('college')
		college = College.objects.get(pk=pk)
		validated_data['college'] = college
		student = Student.objects.create(**validated_data)
		mocktest1_data['student'] = student
		mocktest1 = MockTest1Serializer(data=mocktest1_data)
		if mocktest1.is_valid():
			mocktest1.save()
			student.save()
		return student

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.email = validated_data.get('email', instance.email)
		instance.dob = validated_data.get('data', instance.dob)
		instance.db_folder = validated_data.get('db_folder', instance.db_folder)
		mocktest1 = MockTest1Serializer(instance.mocktest1, data=dict(
			self._validated_data.get('mocktest1')
		))
		if mocktest1.is_valid():
			mocktest1.save()
			instance.save()
		return instance
