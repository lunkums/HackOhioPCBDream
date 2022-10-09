using TMPro;
using UnityEngine;

public class BuildingNameTag : MonoBehaviour
{
    [SerializeField] private TMP_Text text;
    
    private Transform _transform;

    private void Awake()
    {
        _transform = GetComponent<Transform>();
    }

    private void Start()
    {
        Selector.OnSelect += UpdateNameTag;
    }

    private void Update()
    {
        OrientText();
    }

    public Vector3 Position { set => _transform.position = value; }
    public string NameTag { set => text.text = value; }

    private void UpdateNameTag(IBuilding building)
    {
        text.text = building.Name;
        OrientText();
        _transform.position = building.Position;
    }

    private void OrientText()
    {
        _transform.LookAt(Camera.main.transform);
        _transform.Rotate(new Vector3(0, 180, 0), Space.Self);
    }
}
